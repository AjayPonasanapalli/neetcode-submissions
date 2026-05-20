class StockSpanner:

    def __init__(self):
        self.spanner = []

    def next(self, price: int) -> int:
        if not self.spanner:
            self.spanner.append((price,1))
            count = 1
        else:
            num,idx = self.spanner[-1][0],self.spanner[-1][1]
            if not self.spanner or price < num:
                count = 1
                self.spanner.append((price,1))
            else:
                count = 1
                while self.spanner and price>=self.spanner[-1][0] :
                    num,idx = self.spanner[-1][0],self.spanner[-1][1]
                    self.spanner.pop()
                    count+=idx
                
                self.spanner.append((price,count))
                # count +=idx
        print(self.spanner)
        return count

                    



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)