class LinearModel(): #theta, iterations, alpha):

    def add_segment(self):
        ones = np.ones(self.X.shape[0])
        ones=pd.DataFrame(ones)    
        ones = ones.rename(columns = { 0: "const"})
        self.X = pd.concat([ones,self.X],axis = 1)   
        return self.X                     
    

    
    def __init__(self,X,y):
        self.X = add_segment(X)          # 　インスタンス生成時に切片に対応する行を追加する。
        self.y = y           

    


    def inner_product(self):
        return np.dot(self.X,self.theta) 


    def compute_cost(self,theta): 
        self.init_theta = theta      # 初期値のthetaを保存しておく。
        self.theta = theta              # 更新していくthetaはこちら。
        h = inner_product(self.X,self.theta)
        self.error = ((h - np.array(self.y))**2).sum()/(len(self.y)*2)
        return  self.error


        
    def gradient_descent(self,iterations, alpha):
        """
        勾配降下法の処理
        """
        self.count = 0            # イテレーションやハイパーパラメーターを変えて何度も試したりするように、実行回数をカウントする用の変数を用意。
        
        self.past_cost_n = []
        self.past_thetas_n = []
        self.Min_costs = []
        self.opt_thetas = []
        
        if (self.count == 0):

            self.theta = np.reshape(self.theta,(len(self.theta),1))     # thetaのshape調整
            past_costs = []
            past_thetas = []

            # イテレーションや学習係数を修正するたびに初期化をしたくはないので、self.iterationやself.alphaという変数は用意しないことにする。

            cost = compute_cost(self.X,self.y,self.theta)

            past_costs.append(cost)
            past_thetas.append(self.theta)

            for i in range(iterations):
                h = inner_product(self.X,self.theta)

                #  h が(1168,)行列なので、(1168,1)行列にreshape
                #  y は(1168,1)行列なのでそのまま
                #y=np.reshape(np.array(y),(len(h),1))    
                h = np.reshape(h,(len(h),1))

                #(3,1168)と(1168,1)で行列積をして (3,1)行列の　cost関数の微分ベクトルを求める。
                partial_cost = np.dot(self.X.T,(np.array(h)-self.y))


                self.theta = self.theta - (alpha/len(self.y))*partial_cost

                cost = compute_cost(self.X,self.y,self.theta)
                past_costs.append(cost)
                past_thetas.append(self.theta)


                
            self.past_cost_n.append(past_costs)
            self.past_thetas_n.append(past_thetas)
            self.Min_costs.append(min(self.past_cost_n[self.count]))
            
            
            Min_theta_index = min(np.where(self.past_cost_n[self.count] == self.Min_costs[self.count]))
            Min_theta_index =  int(Min_theta_index)
            self.opt_thetas.append(past_thetas[Min_theta_index])

            self.count += 1

            return plt.plot(past_costs)

                  

        else:
            self.theta = init_theta
            self.theta = np.reshape(self.theta,(len(self.theta),1))     # thetaのshape調整
            past_costs = []
            past_thetas = []

            # イテレーションや学習係数を修正するたびに初期化をしたくはないので、self.iterationやself.alphaという変数は用意しないことにする。

            cost = compute_cost(self.X,self.y,self.theta)

            past_costs.append(cost)
            past_thetas.append(self.theta)

            for i in range(iterations):
                h = inner_product(self.X,self.theta)

                #  h が(1168,)行列なので、(1168,1)行列にreshape
                #  y は(1168,1)行列なのでそのまま
                #y=np.reshape(np.array(y),(len(h),1))    
                h = np.reshape(h,(len(h),1))

                #(3,1168)と(1168,1)で行列積をして (3,1)行列の　cost関数の微分ベクトルを求める。
                partial_cost = np.dot(self.X.T,(np.array(h)-self.y))


                self.theta = self.theta - (alpha/len(self.y))*partial_cost

                cost = compute_cost(self.X,self.y,self.theta)
                past_costs.append(cost)
                past_thetas.append(self.theta)


            

            self.past_cost_n.append(past_costs)
            self.past_thetas_n.append(past_thetas)
            self.Min_costs.append(min(self.past_cost_n[self.count]))
            
            
            Min_theta_index = min(np.where(self.past_cost_n[self.count] == self.Min_costs[self.count]))
            Min_theta_index =  int(Min_theta_index)
            self.opt_thetas.append(past_thetas[Min_theta_index])

            plt.plot(past_costs_n[count])
            self.count += 1

            return 0
 

                  

          
        
#      わざわざ関数化する必要がない。.attributeで呼び出せる
#     def Min_cost():
#         return self.Min_cost

#     def past_costs():              
#         return self.past_costs

#     def past_thetas():
#         return self.past_thetas
                  
#     def optimized_theta():
#         return self.opt_theta
                  
#  過去のcost関数の値の遷移のリスト、コスト関数が最小になる時のtheta、thetaの遷移、最小のコストの値を返す。
