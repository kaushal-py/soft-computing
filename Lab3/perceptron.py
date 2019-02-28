class Perceptron():


    def __init__(self, input_size, alpha=1, threshold = 0.2):
        
        # Parse the input file
        # input_size = self._load_file(input_file_path)

        self.weights = [0] * input_size
        self.bias = 0
        self.alpha = alpha
        self.threshold = threshold


    def _load_file(self, input_file_path):
        
        f = open(input_file_path, 'r')



    def _activate(self, y_in):
        
        if y_in > self.threshold:
            return 1
        
        elif y_in <= self.threshold and y_in >= -self.threshold:
            return 0
        
        elif y_in < -self.threshold:
            return -1
    

    def _run_input(self, input_vector, target):
        
        assert len(input_vector) == len(self.weights)

        y_in=self.bias
        for i in range(len(input_vector)):
            y_in += input_vector[i] * self.weights[i]
        
        y = self._activate(y_in)

        if y != target:  
            self._update_weights(input_vector, target)
            # Return true if the input changed the weights
            return True
        else:
            # Return false if input did not change the weights
            return False

    
    def _update_weights(self, input_vector, target):

        self.bias += self.alpha*target
        
        for i in range(len(self.weights)):
            self.weights[i] += self.alpha*target*input_vector[i]
        
    

    def _run_epoch(self, input_matrix, target_vector):
        
        assert len(input_matrix) == len(target_vector)

        flag = False

        for i in range(len(input_matrix)):
            weights_updated = self._run_input(input_matrix[i], target_vector[i])
        
            if weights_updated:
                flag=True
        

        if flag:
            # return true if any input updated the weight (more passes needed)
            return True
        else:
            return False


    def train(self):
        #train
        pass
    

    def output_weights(self):

        for i in range(len(self.weights)):
            print("w{} = {}".format(i, self.weights[i]))
        
        print("b  = {}".format(self.bias))

        print("================")


if __name__ == "__main__":
    p = Perceptron(2)

    for i in range(5):

        print("Epoch {}".format(i+1))

        # p.output_weights()
        p._run_input([1, 1], 1)

        p.output_weights()
        p._run_input([1, 0], 1)

        p.output_weights()
        p._run_input([0, 1], 1)

        p.output_weights()
        p._run_input([0, 0], -1)

        p.output_weights()
    