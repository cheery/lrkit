def snippet(start, stop, source):
    cut1 = max(0, source.rfind('\n', 0, start)+1)
    cut2 = source.find('\n', stop)
    if cut2 == -1:
        cut2 = len(source)
    prefix  = source[cut1:start]
    marker  = source[start:stop]
    postfix = source[stop:cut2]
    snip    = ''.join((prefix, marker, postfix)).strip()
    lastl   = source.rfind('\n', cut1, cut2-1)+1 + cut1
    if start < stop:
        stop -= 1
    return '\n'.join((
        ' ' * (start - cut1) + '.',
        snip,
        ' ' * (stop - lastl) + "^"))
