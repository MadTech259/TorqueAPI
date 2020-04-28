import json
import heapq

import configuration





class ScoreManager:
    def __init__(self):
        self.serializable_file = configuration.filename
        self.score_heap = []
        self.score_dict = {}

    def heap_insert(self, score):
        heapq.heappush(self.score_heap, (int(score["puntos"]), score))

    def insert_score(self, score):
        name = score['nombre']
        if (name in self.score_dict):
            if int(self.score_dict[name]['puntos']) < int(score['puntos']):
                self.score_dict[name] = score
                self.heap_insert(score)
        else:
            self.score_dict[name] = score
            self.heap_insert(score)

        return self.score_dict[name]




    def get_leaderboard(self):
        temp_heap = self.score_heap[:] #List slicing is the fastest way to clone a list https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
        scores = [heapq.heappop(temp_heap) for i in range(len(temp_heap))]
        dict = {"board": scores}
        return dict




        #scores = []
        #for i in self.score_dict:
        #    scores.append(self.score_dict[i])
        #dict = {"board": scores}
        #return dict
