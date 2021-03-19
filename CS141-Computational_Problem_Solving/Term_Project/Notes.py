for b in range(8):
    tock = 0
    for a in range(8):
        if self.__board[a][b] == 1:
            tock += 1
        if (self.__board[a][b] == -1) or (self.__board[a][b] == 2):
            if tock >= 4:
                e = a
                r = b
                self.__score += tock
                break
            else:
                tock = 0
    if tock >= 4:
        while tock > 0:
            self.__board[e-tock][r] = -1
            tock -= 1

#IMPORTANT
x = randint(0,7)
y = randint(0,7)
self.__board[x][y] = 2

#
if self.__once == True:
    self.__score = self.__score + (counter*2)
else:
    self.__score += counter
self.__once = False
counter = 0


#DLR check
    def dlrcheck(self,row,col):#Maybe check in four directions
        tack = 0
        a = row
        b = col
        q = row
        w = col
        while (a >= 0) and (b >= 0):
            a -= 1
            b -= 1
            if self.__board[a][b] == 1:
                tack += 1
            else:
                break
        a = row
        b = col
        while (a <= 7) and (b >= 7):
            a += 1
            b += 1
            if self.__board[a][b] == 1:
                tack += 1
                q = a
                w = b
            else:
                break
        if tack >= 3:
            self.__counter += tack
            while (tack > -1):
                tack -= 1
                self.__board[q][w] = -1
                q -= 1
                w -= 1

        # a = 1
        # b = 1
        # while  (0 <= (row + a) <= 7) and (0 <= (col + b) <= 7):
        #     if self.__board[row + a][col + b] == 1:
        #         self.__drow1list.append(row + a)
        #         self.__dcol1list.append(col + b)
        #         a += 1
        #         b += 1
        #         tack += 1


    # def drlcheck(self,row,col):
    #     tack = 0
    #     a = 0
    #     b = 0
        # while self.__board[row + a][col + b] == 1:
        #     self.__drow2list.append(row + a)
        #     self.__dcol2list.append(col + b)
        #     a -= 1
        #     b += 1
        #     tack += 1
    #     a = 1
    #     b = -1
        # while self.__board[row + a][col + b] == 1:
        #     self.__drow2list.append(row + a)
        #     self.__dcol2list.append(col + b)
        #     a += 1
        #     b -= 1
        #     tack += 1
    #     if tack > 3:
    #         self.__counter += tack
    #         tack = 0
    #     else:
    #         self.__drow2list.clear()
    #         self.__dcol2list.clear()


        # if len(self.__drow2list) > 3:
        #     for r,c in zip(self.__drow2list,self.__dcol2list):
        #         self.__board[r][c] = -1
        #     self.__drow2list.clear()
        #     self.__dcol2list.clear()

        self.__board = [[2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2]]
