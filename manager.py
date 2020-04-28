import json
import heapq

import configuration





class ScoreManager:
    def __init__(self):
        self.serialized_heap = configuration.heap_file
        self.serialized_dict = configuration.dict_file
        self.score_heap = []
        self.score_dict = {}
        self.load_data()


    def serialize(self):
        heap_str = json.dumps(self.score_heap)
        dict_str = json.dumps(self.score_dict)

        f = open(self.serialized_heap, "w")
        f.write(heap_str)
        f.close()

        f = open(self.serialized_dict, "w")
        f.write(dict_str)
        f.close()


    def load_data(self):
        f = open(self.serialized_heap, "r")
        str = f.read()
        f.close()
        if(str != ""):
            self.score_heap = json.loads(str)

        f = open(self.serialized_dict, "r")
        str = f.read()
        f.close()
        if (str != ""):
            self.score_dict = json.loads(str)


    def heap_insert(self, score):
        heapq.heappush(self.score_heap, (int(score["puntos"]), score))
        self.serialize()

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
