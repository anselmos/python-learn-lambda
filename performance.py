import random
import timeit

class LambdaPerformance(object):
    a = [random.random() * 100 for x in range(10)]
    b = [random.random() * 100 for x in range(10)]
    c = [random.random() * 100 for x in range(10)]

    def get_a(self):
        return [80.52714217185243, 8.582268860306607, 41.24644287272067, 57.14549066502261, 90.13396016468924, 70.78398063861876, 49.42469541736204, 50.83021524524571, 91.64036872490283, 43.94296929236723]

    def get_b(self):
        return [48.410516983096045, 93.57910888499613, 88.74192514458217, 49.47449925464254, 45.618293266877465, 37.92400748791912, 0.9403509785295139, 96.51182066063484, 67.71279347122244, 3.971981488965659]

    def get_c(self):
        return [20.121668506632407, 48.319320151552795, 66.28046314491979, 35.152971368158205, 40.835495295932866, 14.826772496643814, 20.769071339195687, 7.85767848903236, 80.98277117190685, 92.75719177433194]

    def test_sum_lambda1(self):
        return map(lambda x,y,z: x+y+z, self.get_a(), self.get_b(), self.get_c())

    def test_sum_lambda1_random(self):
        return map(lambda x,y,z: x+y+z, self.a, self.b, self.c)

    def test_sum_lambda2(self):
        def lam(x,y,z): return x+y+z
        return map(lam, self.get_a(), self.get_b(), self.get_c())

    def test_sum_lambda2_random(self):
        def lam(x,y,z): return x+y+z
        return map(lam, self.a, self.b, self.c)

    def test_multiply_lambda1(self):
        return map(lambda x,y,z: x*y*z, self.get_a(), self.get_b(), self.get_c())

    def test_multiply_lambda2(self):
        def lam(x,y,z): return x*y*z
        return map(lam, self.get_a(), self.get_b(), self.get_c())

    def print_them(self):
        print self.a
        print self.b
        print self.c


times = 100000

time_lambda = (timeit.timeit("obj = LambdaPerformance(); obj.test_sum_lambda1()", setup="from __main__ import LambdaPerformance", number=times))
time_func = (timeit.timeit("obj = LambdaPerformance(); obj.test_sum_lambda2()", setup="from __main__ import LambdaPerformance", number=times))
if time_lambda < time_func:
    print "sum lambda !"
else:
    print "sum func !"
print time_lambda - time_func

time_lambda = (timeit.timeit("obj = LambdaPerformance(); obj.test_multiply_lambda1()", setup="from __main__ import LambdaPerformance", number=times))
time_func = (timeit.timeit("obj = LambdaPerformance(); obj.test_multiply_lambda2()", setup="from __main__ import LambdaPerformance", number=times))

if time_lambda < time_func:
    print "multiply lambda !"
else:
    print "multiply func !"
print time_lambda - time_func
