def min_key(d : dict) :
    return min(d, key=d.get)
class Grid() :
    def __init__(self, n : int, tiles : list[str,int], dependencies : dict[(str,int):dict[str:list[str,int]]] = None, distribution : dict = None):
        """generate a n by n grid to apply the wave function collapse algorithm to

        Args:
            n (int): nuber of tiles making the sides of the grid 
            tiles (list[str,int]): list of objects indexing your tiles (the elements of this list are what will be returned when indexing the final grid)
            dependencies (dict of dicts of lists): dict holding all the tiles dependencies. Keys of the first dict must be all the elements of tiles and refer to dicts with keys "up","down","left","right", each one referring a list of tiles that can be put in that position relative to the tile in the first key. 
                                                    Defaults to None. If left as None, all tiles will be allowed to be next to each other
            distribution (dict): dict holding the probability for each tile to appear. Keys must be all the elements of tiles refering to the probability of it appearing. Defaults to None. If set to None all tiles will have the same probability of appearing
        """
        self.grid = {}
        
        self.uncertainties = {}
        
        self.adjacent = {}
        
        l=len(dependencies)
        for i in range(n) :
            for j in range(n) :
                self.uncertainties[i,j] = l
                self.grid[i,j] = tiles
                self.adjacent[i,j] = {}
                
                if i==0 :
                    self.adjacent[i,j]["right"] = [i+1,j]
                elif i==n-1 :
                    self.adjacent[i,j]["left"] = [i-1,j]
                else :
                    self.adjacent[i,j]["right"] = [i+1,j]
                    self.adjacent[i,j]["left"] = [i-1,j]
                
                if j==0 :
                    self.adjacent[i,j]["up"] = [i,j+1]
                elif j==n :
                    self.adjacent[i,j]["down"] = [i,j-1]
                else :
                    self.adjacent[i,j]["up"] = [i,j+1]
                    self.adjacent[i,j]["down"] = [i,j-1]
                    
        
        self.dependencies = dependencies
        
        self.distribution = distribution
        
        if not dependencies :
            self.dependencies = dict((tile,dict((pos,tiles) for pos in ["up","down","right","left"])) for tile in tiles)
            
        if not distribution :
            self.distribution = dict((tile,1) for tile in tiles)
            
        
        self.__origins={"up":"down","down":"up","right":"left","left":"right"}
    
    def reccollapse(self,updater : tuple[int,int], current : tuple[int,int], update_direction : str) -> None|str :
        ref=len(self.grid[current])
        compare(updater,current,update_direction)
        new=len(self.grid[current])
        if new==0 :
            return "error : unsolvable pattern happened"
        if new!=ref :
            for e in self.adjacent[current] :
                catch=self.reccollapse(current, self.adjacent[current][e], self.__origins[e])
                return catch