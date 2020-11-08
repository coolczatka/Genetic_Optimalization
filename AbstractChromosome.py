
class AbstractChromosome:
    def cross(self, chromB):
        raise NotImplementedError('NI')

    def mutate(self):
        raise NotImplementedError('NI')

    #ChromosomeConfig
    def setConfig(self, config):
        self.config = config
