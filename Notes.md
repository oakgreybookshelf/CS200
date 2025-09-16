LIFO vs. FILO--------------------------------------

Structure holds [first] element and a FIFO [buffer].
There is a helper function for total count.

push [a]:
If total count is 0, write [a] to [first].
Push [a] to [buffer] otherwise.

pop:
If total count is 1, return [first].
Pop from [buffer] otherwise.
(If total count is 0, throw exception or whatever.)
