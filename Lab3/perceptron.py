import time
from beautifultable import BeautifulTable

class Perceptron:

    def __init__(self, input_file_path, input_length, alpha=1, threshold = 0.2):
        
        # Parse the input file
        self.input_matrix = []
        self.target_vector = []

        self._load_file(input_file_path, input_length)

        self.weights = [0] * len(self.input_matrix[0])
        self.bias = 0
        self.alpha = alpha
        self.threshold = threshold


    def _load_file(self, input_file_path, input_length):
        
        f = open(input_file_path, 'r')
        lines = f.readlines()
        # print(lines)
        num_ip = int(lines[0])
        
        i=1
        for j in range(num_ip):

            target = int(lines[i])
            input_vector = []
            for k in range(1,input_length+1):

                for x in lines[i+k][:-1].split(' '):
                    input_vector.append(self._pattern(x))
            
            i+=(input_length+1)

            self.input_matrix.append(input_vector)
            self.target_vector.append(target)

        print(self.input_matrix, self.target_vector)

        print("SUCCESS: Parsing of input successful.")

    
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
        
    

    def _run_epoch(self, epoch):

        assert len(self.input_matrix) == len(self.target_vector)

        flag = False
        count_updated_inputs = 0

        for i in range(len(self.input_matrix)):
            weights_updated = self._run_input(self.input_matrix[i], self.target_vector[i])
            # self.output_weights()
            if weights_updated:
                count_updated_inputs += 1
                flag=True
        
        print("\n=== Epoch {} Summary ===\n".format(epoch))
        print("Table : Weights after epoch {}".format(epoch))
        self.output_weights()
        print("Number of inputs that updated weights : {}".format(count_updated_inputs))


        if flag:
            # return true if any input updated the weight (more passes needed)
            return True
        else:
            return False


    def train(self):

        print("========== Training phase ===========")
        
        start = time.clock()
        stop_train = False

        epoch = 1

        while not stop_train:
            # print(epoch)
            train = self._run_epoch(epoch)
            stop_train = not train
            epoch += 1

        print("\n" + '-'*50)

        print("\t\tFINAL TRAINED WEIGHTS")
        self.output_weights()

        print("\nTraining completed after : {} epochs".format(epoch-1))
        end =  time.clock()
        print("Total time taken for training : {:.2} sec".format(end-start))


    def output_weights(self):

        table = BeautifulTable()
        table.column_headers = ['w'+str(i) for i in range(1, len(self.weights)+1)]
        table.append_row(self.weights)

        table.append_column("b", [self.bias])
        print(table)


if __name__ == "__main__":
    p = Perceptron("Lab3/pattern.txt", 3)
    # p = Perceptron("Lab3/and.txt", 1)
    p.train()
    