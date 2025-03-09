import numpy as np

class node:
    def __init__(self, featureindex=None, thresh=None, lchild=None, rchild=None, predictedclass=None):
        self.featureindex = featureindex
        self.thresh=thresh
        self.lchild=lchild
        self.rchild= rchild
        self.predictedclass= predictedclass

class decisiontree:
    def __init__(self, criterion='entropy'):
        self.criterion = criterion
        self.root = None

    
    def fit(self, X, y):
        self.root = self.buildtree(X, y)

    
    def buildtree(self, X, y):
        
        if len(np.unique(y)) == 1:
            return node(predictedclass=y[0])
        if X.shape[0] == 0:
            return None
        
        featureindex, value, bestgain, leftidx, rightidx = self.bestsplit(X, y)
        if featureindex is None or len(leftidx) == 0 or len(rightidx) == 0:
            majorityclass= self.majorityclass(y)
            return node(predictedclass=majorityclass)
        leftsubtree=self.buildtree(X[leftidx], y[leftidx])
        rightsubtree =self.buildtree(X[rightidx], y[rightidx])
        return node(featureindex=featureindex, thresh=value, lchild=leftsubtree, rchild=rightsubtree)

    def bestsplit(self, X, y):
        bestgain = -1
        bestfeatureindex =None
        bestvalue= None
        bestleftidx= None
        bestrightidx = None
        currententropy = self.entropy(y)
        nsamples, nfeatures = X.shape
        for i in range(nfeatures):
            values = np.unique(X[:, i])
            for val in values:
                leftidx = np.where(X[:, i] == val)[0]
                rightidx = np.where(X[:, i] != val)[0]
                if len(leftidx)== 0 or len(rightidx)==0:
                    continue
                lent=len(leftidx)
                ren=len(rightidx)
                leftentropy= self.entropy(y[leftidx])
                rightentropy= self.entropy(y[rightidx])
                weightedentropy =(lent / nsamples) * leftentropy + (ren / nsamples) * rightentropy
                gain=currententropy-weightedentropy
                if gain>bestgain:
                    bestgain = gain
                    bestfeatureindex = i
                    bestvalue = val
                    bestleftidx = leftidx
                    bestrightidx = rightidx
        return bestfeatureindex, bestvalue, bestgain, bestleftidx, bestrightidx

    def entropy(self, y):
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / counts.sum()
        ent = -np.sum(probabilities * np.log2(probabilities + 1e-9))
        return ent

    def majorityclass(self, y):
        classes, counts = np.unique(y, return_counts=True)
        return classes[np.argmax(counts)]

    def predict(self, X):
        return np.array([self.predictsample(x, self.root) for x in X])

    def predictsample(self, x, n):
        if n.predictedclass is not None:
            return n.predictedclass
        if x[n.featureindex] == n.thresh:
            return self.predictsample(x, n.lchild)
        else:
            return self.predictsample(x, n.rchild)


X = np.array([[0, 2, 1],
            [1, 1, 0],
              [2, 2, 1],
              [0, 1, 0],
              [1, 2, 1]])

y = np.array([1, 0, 1, 0, 1])

clf = decisiontree(criterion='entropy')

clf.fit(X, y)
newsample = np.array([[0, 2, 0]])
prediction = clf.predict(newsample)
print("Prediction:", prediction[0])
