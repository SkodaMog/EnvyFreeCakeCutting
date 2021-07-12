"""
/**
 * Simple agent class for my implementations of envy free procedures
 *
 * @author Thomas Gibson
 * @date 30/04/2021
 */
"""




class Agent:
    def __init__(self, name, atomvaluations):
        self.name = name
        self.vals = atomvaluations
        self.allocation = 0
        self.trim = 0
        self.holdingtrimmed = 0
        self.totalallocation = 0
        self.totalvalue = 0
        self.cutter = 0
        self.mark = 0