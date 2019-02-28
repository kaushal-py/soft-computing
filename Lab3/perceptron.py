class Perceptron:

    def __init__(self, input_file_path, alpha=1, threshold = 0.2):
        
        # Parse the input file
        self.input_matrix = []
        self.target_vector = []

        self._load_file(input_file_path)

        self.weights = [0] * len(self.input_matrix[0])
        self.bias = 0
        self.alpha = alpha
        self.threshold = threshold


    def _load_file(self, input_file_path):
        
        f = open(input_file_path, 'r')
        lines = f.readlines()
        # print(lines)
        num_ip = int(lines[0])
        
        i=1
        for j in range(num_ip):

            target = int(lines[i])
            input_vector = []
            for k in range(1,4):

                for x in lines[i+k][:-1].split(' '):
                    input_vector.append(self._pattern(x))
            
            i+=4

            self.input_matrix.append(input_vector)
            self.target_vector.append(target)

        print(self.input_matrix, self.target_vector)

    
    def _pattern(self, x):

        if x=='*':
            return 1
        elif x=='.':
            return -1


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
        
    

    def _run_epoch(self):
        
        assert len(self.input_matrix) == len(self.target_vector)

        flag = False

        for i in range(len(self.input_matrix)):
            weights_updated = self._run_input(self.input_matrix[i], self.target_vector[i])
        
            if weights_updated:
                flag=True
        

        if flag:
            # return true if any input updated the weight (more passes needed)
            return True
        else:
            return False


    def train(self):
        
        stop_train = False

        epoch = 1

        while not stop_train:
            print(epoch)
            train = self._run_epoch()
            stop_train = not train
            epoch += 1
    

    def output_weights(self):

        for i in range(len(self.weights)):
            print("w{} = {}".format(i, self.weights[i]))
        
        print("b  = {}".format(self.bias))

        print("================")


if __name__ == "__main__":
    p = Perceptron("Lab3/input.txt")
    p.train()
    p.output_weights()
    