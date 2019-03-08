class Hopfield():

    def __init__(self, input, missing):
        '''
        input : Input vector for which we need to construct the hopfield network
        missing : Vector specifying which inputs are missing. Used for testing the network

        For eg. if the input vector is [1 1 1 -1]
        If the first and second entries are missing then the missing vector will be [1 1 0 0]
        The net testing input is calculated by placing 0s at places where the input is missing.
        Therefore the missing input vector becomes [ 0 0 1 0]
        '''

        self.input = input
        self.missing = missing

    def calc_weight_matrix(self):

        self.weight_matrix = [[0 for i in range(len(self.input))] for j in range(len(self.input))]

        for i in range(len(self.input)):
            for j in range(len(self.input)):

                if i!=j:
                    self.weight_matrix[i][j] = self.input[i]*self.input[j]
                

        # print(weight_matrix)


if __name__ == "__main__":
    
    h = Hopfield([1,1,1,-1], [1,1,0,0])
    h.calc_weight_matrix()
        