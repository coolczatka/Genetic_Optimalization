class Specimen:
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness

    def __str__(self):
        string = "Genome: "
        for x in self.genome:
            string = string + str(x) + " "

        string = string + " Value: " + str(self.fitness)
        return string
