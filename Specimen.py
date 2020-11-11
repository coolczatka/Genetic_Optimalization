class Specimen:
    def __init__(self, genome, value):
        self.genome = genome
        self.value = value

    def __str__(self):
        string = "Genome: "
        for x in self.genome:
            string = string + str(x) + " "

        string = string + " Value: " + str(self.value)
        return string
