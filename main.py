import math


class Lift:
    def __init__(self, low_reps='Epley', medium_reps='Epley', high_reps='Epley', ever_trained=0):
        self.low_reps = low_reps
        self.medium_reps = medium_reps
        self.high_reps = high_reps
        self.ever_trained = ever_trained

    def __str__(self):
        if self.ever_trained == 0:
            return 'The algorithm for this movement has not yet been trained'
        elif self.ever_trained == 1:
            return f'This movement is currently being calculated using the {self.low_reps} formula for low reps, the {self.medium_reps} formula for medium reps and the {self.high_reps} formula for high reps.'

    def train_algorithm(self, one_rm, weight, reps):
        epley = weight * (1 + (reps / 30))
        brzycki = weight * (1.0278 - 0.0278 * reps)
        lombardi = weight * reps ** 0.10
        mcglothin = (100 * weight) / (101.3 - 2.67123 * reps)
        mayhew = 100 * weight / (52.2 + 41.9 * math.exp(-0.055 * reps))
        oconner = weight * (1 + reps / 40)
        wathen = 100 * weight / (48.8 + 53.8 * math.exp(-0.075 * reps))
        list_formulas = ['Epley', 'Brzycki', 'Lombardi', 'McGlothin', 'Mayhew', "O'Conner", 'Wathen']
        difference_chart = [abs(epley - one_rm), abs(brzycki - one_rm), abs(lombardi - one_rm), abs(mcglothin - one_rm),
                            abs(mayhew - one_rm), abs(oconner - one_rm), abs(wathen - one_rm)]
        minimum_deviance = difference_chart.index(min(difference_chart))
        if reps < 5:
            self.low_reps = str(list_formulas[minimum_deviance])
        elif 5 <= reps < 8:
            self.medium_reps = str(list_formulas[minimum_deviance])
        if 8 <= reps:
            self.high_reps = str(list_formulas[minimum_deviance])
        self.ever_trained = 1
        return str(list_formulas[minimum_deviance])

    def onerm_calc(self, weight, reps):
        if reps < 5:
            algo = self.low_reps
        elif 5 <= reps < 8:
            algo = self.medium_reps
        if 8 <= reps:
            algo = self.high_reps
        if algo == 'Epley':
            return (weight * (1 + (reps / 30)))
        elif algo == 'Brzycki':
            return (weight * (1.0278 - 0.0278 * reps))
        elif algo == 'Lombardi':
            return (weight * reps ** 0.10)
        elif algo == 'McGlothin':
            return ((100 * weight) / (101.3 - 2.67123 * reps))
        elif algo == 'Mayhew':
            return (100 * weight / (52.2 + 41.9 * math.exp(-0.055 * reps)))
        elif algo == "O'Conner":
            return (weight * (1 + reps / 40))
        elif algo == 'Wathen':
            return (100 * weight / (48.8 + 53.8 * math.exp(-0.075 * reps)))

def choose_lift():
    lift = str(input('Which lift do you want to analyze? s/b/d: ')).strip()
    if lift == 's':
        return 's'
    elif lift == 'b':
        return 'b'
    elif lift == 'd':
        return 'd'


squat = Lift()
bench = Lift()
deadlift = Lift()


command = str(input('Would you like to train your algorithm or calculate a new 1RM? t/c: ')).strip()
while True:
    if command == 't':
        lift = choose_lift()
        one_rm = int(input('Please input your most recently tested 1RM: '))
        high_Rep_weight = int(input('How much weight did you use for a recent high rep set? '))
        reps = int(input('How many reps did you achieve at that weight? '))
        if lift == 's':
            result = squat.train_algorithm(one_rm, high_Rep_weight, reps)
        elif lift == 'b':
            result = bench.train_algorithm(one_rm,high_Rep_weight,reps)
        elif lift == 'd':
            result = deadlift.train_algorithm(one_rm, high_Rep_weight, reps)
        print(f'The algorithm has been trained. For the lift and rep range in analysis, the model has been approximated to the {result} formula. ')
    elif command == 'c':
        lift = choose_lift()
        high_Rep_weight = int(input('How much weight did you use for your multiple rep set? '))
        reps = int(input('How many reps did you achieve at that weight? '))
        print(f'Your estimated 1RM is {round(bench.onerm_calc(high_Rep_weight,reps),1)}')
    elif command == 'q':
        exit()
    command = str(input('Would you like to train your algorithm, calculate a new 1RM or quit? t/c/q: ')).strip()