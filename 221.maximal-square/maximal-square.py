class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, max_size = len(matrix), 0
        '''
        size[i]: the current number of continuous '1's in a column of matrix. Reset when discontinued.
        The idea is to do a by-row scan, updating size[i]
        Then check if there are continuous elements in size whose value is bigger than current maximal size.
        '''
        if rows > 0:
            cols = len(matrix[0])
            size = [0] * cols
            for x in xrange(rows):
                # update size
                count, size = 0, map(lambda x, y: x+1 if y == '1' else 0, size, matrix[x])
                for y in xrange(cols):
                    # check if it exceeds current maximal size
                    if size[y] > max_size:
                        count += 1
                        if count > max_size:
                            # increase maximal size by 1
                            max_size += 1
                            break
                    else:
                        count = 0

        return max_size*max_size