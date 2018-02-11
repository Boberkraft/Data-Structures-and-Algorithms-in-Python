from PositinalList import PositionalList

def insertion_sort(l):
    if len(l) > 1:
        marker = L.first()
        while marker != l.last():
            pivot = l.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != l.first() and l.before(walk).element() > value:
                    walk = l.before(walk)
                l.delete(pivot)
                l.add_before(walk, value)