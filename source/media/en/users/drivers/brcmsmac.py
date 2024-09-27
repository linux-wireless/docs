import tracecmd
import struct


# Default amount of padding to add to the left of strings being printed
# to the trace output
PAD = 60

# Print a string to the trace buffer output with reasonable alignment.
# Really should only be used for lines of a multi-line print after the
# first.
def trace_puts(trace_seq, s):
    trace_seq.puts("%*s %s" % (PAD, "", s))

# Version of trace_puts which adds extra padding
def trace_puts_pad(trace_seq, pad, s):
    trace_seq.puts("%*s %s" % (PAD + pad, "", s))


# Pretty-print a bitfield. Takes as an argument a bitfield (bf) and a list
# of descriptions. The elements of the description list is another list
# with the following items (in order):
#
#  - Start bit for the field
#  - Number of bits for the field
#  - Short description (i.e. name) of the field
#  - Long description of the field
def print_bitfield(trace_seq, pad, bf, descs):
    for desc in descs:
        start = desc[0]
        length = desc[1]
        name = desc[2]
        description = desc[3]
        field = (bf >> start) & ((1 << length) - 1)
        if length == 1:
            if field:
                trace_puts_pad(trace_seq, pad, "%-25s (%s)\n" % (name, description))
        else:
            trace_puts_pad(trace_seq, pad, "%-25s %#8x (%s)\n" % (name, field, description))

def dump_hex(trace_seq, pad, data):
    for i in range(len(data)):
        if (i % 16) == 0:
            trace_seq.puts("%*s %04x " % (PAD + pad, "", i))
        trace_seq.puts(" %02x" % (data[i]))
        if (i % 16) == 15:
            trace_seq.puts("\n")
    if (i % 16) != 15:
        trace_seq.puts("\n")

def macintstatus_event_handler(pevent, trace_seq, event):
    macint_descs = [
            [0,  1, "MI_MACSSPNDD",  "MAC suspended"],
            [1,  1, "MI_BCNTPL", "beacon template available"],
            [2,  1, "MI_TBTT", "TBTT indication"],
            [3,  1, "MI_BCNSUCCESS", "successful beacon tx"],
            [4,  1, "MI_BCNCANCLD", "IBSS beacon cancele"],
            [5,  1, "MI_ATIMWINEND", "end of ATIM window"],
            [6,  1, "MI_PMQ", "PMQ entries available"],
            [7,  1, "MI_NSPECGEN_0", "PSM gen-stat bit 0"],
            [8,  1, "MI_NSPECGEN_1", "PSM gen-stat bit 1"],
            [9,  1, "MI_MACTXERR", "MAC level tx error"],
            [10, 1, "MI_NSPECGEN_3", "PSM gen-stat bit 3"],
            [11, 1, "MI_PHYTXERR", "PHY tx error"],
            [12, 1, "MI_PME", "power management event"],
            [13, 1, "MI_GP0", "general-purpose timer 0"],
            [14, 1, "MI_GP1", "general-purpose timer 1"],
            [15, 1, "MI_DMAINT", "DMA interrupt"],
            [16, 1, "MI_TXSTP", "TX fifo suspend complete"],
            [17, 1, "MI_CCA", "CCA measurement complete"],
            [18, 1, "MI_BG_NOISE", "background noise sample collection complete"],
            [19, 1, "MI_DTIM_TBTT", "MBSS DTIM TBTT indication"],
            [20, 1, "MI_PRQ", "probe response queue needs attention"],
            [21, 1, "MI_PWRUP", "radio/phy powered up"],
            [22, 1, "MI_RESERVED3", ""],
            [23, 1, "MI_RESERVED2", ""],
            [24, 1, "UNKNOWN", ""],
            [25, 1, "MI_RESERVED1", ""],
            [26, 1, "UNKNOWN", ""],
            [27, 1, "UNKNOWN", ""],
            [28, 1, "MI_RFDISABLE", "RF disable state change"],
            [29, 1, "MI_TFS", "MAC has completed a tx"],
            [30, 1, "MI_PHYCHANGED", "PHY status change wrt G mode"],
            [31, 1, "MI_TO", "general purpose timeout"],
    ]
    field = event['macintstatus']
    macintstatus = long(field)
    in_isr = bool(event['in_isr'])
    trace_seq.puts("[%s] macintstatus %#x, %s\n" % (str(event['dev']), macintstatus, str(in_isr)))
    print_bitfield(trace_seq, 0, macintstatus, macint_descs)


def precenq_event_handler(pevent, trace_seq, event):
    trace_seq.puts("[%s] pktq: prec=%d num_prec=%d hi_prec=%d max=%d len=%d\n" %
        (str(event['dev']), long(event['prec']), long(event['num_prec']),
         long(event['hi_prec']), long(event['max']), long(event['len'])))

    # Unpack the pmax array
    num_prec = long(event['num_prec'])
    fmt = pevent.file_endian + str(num_prec) + 'H'
    pmax = struct.unpack(fmt, event['pmax'].data)

    # Print the number of frames in each precedence queue
    for i in range(num_prec):
        trace_puts(trace_seq, "%s %2d: %d\n" % ("prec", i, pmax[i]))


def txdesc_event_handler(pevent, trace_seq, event):
    if long(event['in']) == 1:
        txdir = "IN"
    else:
        txdir = "OUT"
    # txdesc is supplied in the raw binary format. Unpack the data.
    txh = struct.unpack("<11H16B6BH6BH6B14H6B2H6B6BH", event['txh'].data)
    trace_seq.puts("%s[%s] txdesc:\n" % (txdir, str(event['dev'])))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MacTxControlLow", txh[0]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MacTxControlHigh", txh[1]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MacFrameControl", txh[2]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("TxFesTimeNormal", txh[3]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PhyTxControlWord", txh[4]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PhyTxControlWord_1", txh[5]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PhyTxControlWord_1_Fbr", txh[6]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PhyTxControlWord_1_Rts", txh[7]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PhyTxControlWord_1_FbrRts", txh[8]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MainRates", txh[9]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("XtraFrameTypes", txh[10]))
    trace_puts(trace_seq, "IV:\n")
    dump_hex(trace_seq, 2, txh[11:27])
    trace_puts(trace_seq, "TxFrameRA:\n")
    dump_hex(trace_seq, 2, txh[27:33])
    trace_puts(trace_seq, "%-30s %#x\n" % ("TxFesTimeFallback", txh[33]))
    trace_puts(trace_seq, "RTSPLCPFallback:\n")
    dump_hex(trace_seq, 2, txh[34:40])
    trace_puts(trace_seq, "%-30s %#x\n" % ("RTSDurFallback", txh[40]))
    trace_puts(trace_seq, "FragPLCPFallback:\n")
    dump_hex(trace_seq, 2, txh[41:47])
    trace_puts(trace_seq, "%-30s %#x\n" % ("FragDurFallback", txh[47]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MModeLen", txh[48]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MmodeFbrLen", txh[49]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("TstampLow", txh[50]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("TstampHigh", txh[51]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("ABI_MimoAntSel", txh[52]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("PreloadSize", txh[53]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("AmpduSeqCtl", txh[54]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("TxFrameID", txh[55]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("TxStatus", txh[56]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MaxNMpdus", txh[57]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MaxABytes_MRT", txh[58]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MaxABytes_FBR", txh[59]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("MinMBytes", txh[60]))
    trace_puts(trace_seq, "RTSPhyHeader:\n")
    dump_hex(trace_seq, 2, txh[61:67])
    trace_puts(trace_seq, "%-30s %#x\n" % ("rts_frame.frame_control", txh[67]))
    trace_puts(trace_seq, "%-30s %#x\n" % ("rts_frame.duration", txh[68]))
    trace_puts(trace_seq, "rts_frame.ra:\n")
    dump_hex(trace_seq, 2, txh[69:75])
    trace_puts(trace_seq, "rts_frame.ra:\n")
    dump_hex(trace_seq, 2, txh[75:81])
    # Final element is pad byte


def txstatus_event_handler(pevent, trace_seq, event):
    frameid_descs = [
        [0, 3, "TXFID_QUEUE", "Tx queue"],
        [3, 2, "TXFID_RATE", "Tx rate"],
        [5, 11, "TXFID_SEQ", "Tx sequence"],
    ]
    txstat_descs = [
        [0,  1, "TX_STATUS_VALID", "Tx status valid"],
        [1,  1, "TX_STATUS_ACK_RCV", "ACK received"],
        [2,  3, "TX_STATUS_SUPR", "Suppress status"],
        [5,  1, "TX_STATUS_AMPDU", "AMPDU status"],
        [6,  1, "TX_STATUS_INTERMEDIATE", "Intermediate or 1st ampdu pkg"],
        [7,  1, "TX_STATUS_PMINDCTD", "PM mode indicated to AP"],
        [8,  4, "TX_STATUS_RTS_RTX", "RTS count"],
        [12, 4, "TX_STATUS_FRM_RTX", "Frame count"],
    ]

    framelen = long(event['framelen'])
    frameid = long(event['frameid'])
    status = long(event['status'])
    lasttxtime = long(event['lasttxtime'])
    sequence = long(event['sequence'])
    phyerr = long(event['phyerr'])
    ackphyrxsh = long(event['ackphyrxsh'])
    trace_seq.puts("[%s] frameid=%#x framelen=%d status=%#x lasttxtime=%d sequence=%d phyerr=%#x ackphyrxsh=%#x\n" %
                   (str(event['dev']), frameid, framelen, status, lasttxtime,
                    sequence, phyerr, ackphyrxsh))

    trace_puts(trace_seq, "frame id:\n")
    print_bitfield(trace_seq, 2, frameid, frameid_descs)

    trace_puts(trace_seq, "tx status:\n")
    print_bitfield(trace_seq, 2, status, txstat_descs)


def register(pevent):
    pevent.register_event_handler("brcmsmac", "brcms_macintstatus",
            lambda *args: macintstatus_event_handler(pevent, *args))
    pevent.register_event_handler("brcmsmac", "brcms_prec_enq",
            lambda *args: precenq_event_handler(pevent, *args))
    pevent.register_event_handler("brcmsmac_tx", "brcms_txstatus",
            lambda *args: txstatus_event_handler(pevent, *args))
    pevent.register_event_handler("brcmsmac_tx", "brcms_txdesc",
            lambda *args: txdesc_event_handler(pevent, *args))
