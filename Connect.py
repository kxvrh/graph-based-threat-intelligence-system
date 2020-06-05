from py2neo import Graph, Node, Relationship
import pandas as pd
import csv
import numpy as np
import networkx as nx
import re

'''
ip     domain  url    time    post-data  attack-type
0.339  0.177   0.090  0.291   0.055      0.048
'''

#for node1 in graph.nodes:
    #for node2 in graph.nodes:
def AttrSim(graph):
    for i in range(0, 1010):
        for j in range(i, 1010):
            if(i == j):
                continue
            node1 = graph.nodes[i]
            node2 = graph.nodes[j]
            if(node1["ip"]=="ip" or node2["ip"]=="ip"):
                continue
            sim = 0.0
            if(node1["ip"] == node2["ip"]):
                sim += 0.339
            if(node1["domainName"] == node2["domainName"]):
                sim += 0.177
            if(node1["url"] == node2["url"]):
                sim += 0.090
            if(node1["postData"] == node2["postData"]):
                sim += 0.055
            if(node1["attackType"] == node2["attackType"]):
                sim += 0.048
            time1 = re.search("(.*)T", node1["time"]).group()
            time2 = re.search("(.*)T", node2["time"]).group()
            if(time1 == time2):
                sim += 0.291
            if(sim > 0.35):
                rel = Relationship(node1, "sim", node2)
                rel['sim'] = sim
                graph.merge(rel)
 
def StructSim(graph):
    for i in range(0, 1010):
        for j in range(i, 1010):
            if(i == j):
                continue
            node1 = graph.nodes[i]
            node2 = graph.nodes[j]
            if(node1["ip"]=="ip" or node2["ip"]=="ip"):
                continue
            id1 = node1["id"]
            id2 = node2["id"]
            rel = list(graph.run("match (a:httpRequest)-[r]->(b:httpRequest) where a.id='"+id1+ "'and b.id='"+id2+"' return r.sim"))
            if(len(rel) == 0):
                continue
            for x in rel:
                x = str(x)
                w = re.search('-?\d+\.?\d*e?-?\d*?', x).group()
            w = float(w)
            #print(num)

            rel1 = list(graph.run("match (a:httpRequest)-[r]->() where a.id='"+id1+ "' return r.sim"))
            sum1 = 0
            for x in rel1:
                x = str(x)
                num = re.search('-?\d+\.?\d*e?-?\d*?', x).group()
                sum1 += float(num)
            #print(sum1)

            rel2 = list(graph.run("match (a:httpRequest)-[r]->() where a.id='"+id2+ "' return r.sim"))
            sum2 = 0
            for x in rel2:
                x = str(x)
                num = re.search('-?\d+\.?\d*e?-?\d*?', x).group()
                sum2 += float(num)
            #print(sum2)
            
            aver = 1 / (len(rel1) + len(rel2))
            if(sum1 + sum2 -w) == 0:
                continue
            sim = w / (sum1 + sum2 - w)
            if(sim > aver):
                rel = graph.match_one((node1, node2))
                rel['sim2'] = sim
                graph.push(rel)
            else:
                rel = graph.match_one((node1, node2))
                graph.separate(rel)


            


       
if __name__ == "__main__":
    graph = Graph("bolt://localhost:7687", username="neo4j", password="*****")
    AttrSim(graph)
    StructSim(graph)
    

   