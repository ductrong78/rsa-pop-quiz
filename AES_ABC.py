#!/usr/bin/env python


import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0:
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded


def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n') + 1:]


def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data


def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (chr(padding) * padding)

def aes_abc_decrypt(ct):
    blocks = [ct[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
    new_blocks = []
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i + 1].encode('hex'), 16)

        n_curr_blk = (- prev_blk + curr_blk) % UMAX
        new_blocks.append(to_bytes(n_curr_blk))
    pt_abc = "".join(new_blocks)
    return pt_abc


if __name__ == "__main__":
    with open('body.enc.ppm', 'rb') as f:
        header, data = parse_header_ppm(f)
    c_img = aes_abc_decrypt(data)
    with open('flag.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(c_img)
