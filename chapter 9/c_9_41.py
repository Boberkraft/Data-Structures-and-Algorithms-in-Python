"""
Tamarindo Airlines wants to give a first-class upgrade coupon to their top
logn frequent flyers, based on the number of miles accumulated, where
n is the total number of the airlines’ frequent flyers. The algorithm they
currently use, which runs in O(nlog n) time, sorts the flyers by the number
of miles flown and then scans the sorted list to pick the top logn flyers.
Describe an algorithm that identifies the top logn flyers in O(n) time.

Do bottom-up heap construction basing on the miles flown

and fetch log n elements

there is a catch here, ye?, is there?
"""
