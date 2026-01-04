#足し算(一次元）
three = np.ones(3)
three #array([1., 1., 1.])

three + 3 #array([4., 4., 4.])　個々の要素に等しく足された
three + [1,0,1] #array([2., 1., 2.])

#足し算(多次元）
six_reshape = np.arange(6).reshape(2,3)
#numpy.arangeメソッドで[0, 1, 2, 3, 4, 5]という一次元配列を作成
#numpy.reshapeというメソッドで配列の形状を2x3に変更
#NumPyはメソッドチェーンが使えるため、連続してメソッドを記載する事ができる

six_reshape #array([[0, 1, 2],
                    #[3, 4, 5]])

six_reshape +1 #array([[1, 2, 3],
                        #4, 5, 6]]) 個々の要素に等しく足された

six_reshape + np.array([[1, 0 ,2], [1, 0, 2]]) #array([[1, 1, 4],
                                                        #[4, 4, 7]])

#引き算は、足し算と同じ

#掛け算
five = np.arange(5)
five #array([0,1,2,3,4])

five * 3 #array([0,3,6,9,12])
five*np.array([2,3,4,5,6]) #array([ 0,  3,  8, 15, 24])

#引き算は、{/}を使用したら掛け算と同じ

#行列演算＿行列の積
A = np.array([[4,7,2],[1,2,1]])
B = np.array([[2, 2, 2], [4, 5, 2], [9, 2, 1]])
np.dot(A, B) #array([[54, 47, 24],
                    #[19, 14,  7]])

#合計値
a =np.array([1,2,3])
np.sum(a) #6

a = np.array([[14,8,11,10],[7,9,10,11],[10,15,5,10]])
np.sum(a) #120 全ての合計
np.sum(a,axis=0) #array([31,32,26,31]) 列毎に足す方法
np.sum(a,axis=1)#array([43,37,40])　行ごとに足す方法

#中央値
a = np.array([1,2,3,4])
np.median(a) #2.5

#標準偏差
a = np.array([1,2,3,4,5])
np.std(a) #np.float64(1.4142135623730951)

