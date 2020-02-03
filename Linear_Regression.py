class linear_regression():
    
    def __init__(self, alpha=0.0001, n_iter=50):        
        self.alpha = alpha        
        self.n_iter = n_iter

    def compute_cost(self, x,y):               
        return  np.sum(np.square(x.dot(self.theta)-y)/(2*len(y)))
    
    def gradient_descent(self,x,y):
        cost=[]
        self.theta = np.zeros((X.shape[1],1))
        
        for i in range(self.n_iter):
            self.theta = self.theta - self.alpha*((x.T).dot(x.dot(self.theta)-y))/len(y)
            cost.append(self.compute_cost(x,y))
        return self.theta,cost
    
    def feature_normalize(self,x):
        mu=x.mean(axis=0)
        sigma=x.std(axis=0)
        x_norm = (x-mu)/sigma
        return x_norm
