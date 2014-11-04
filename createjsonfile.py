#encoding=utf-8
import  ujson
import  redis
import random

json=ujson
basedir='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export/'
filenames=["Act.EduInst_hierarchy-entity-cobweb-partitioning_decreasing_20140624-0705-4ldfadv.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning_increasing_20140624-0705-3z6b8kn.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140624-0705-4ldfadv.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140624-0705-3z6b8kn.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_random_20140624-0705-0nbhpj2.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning_random_20140624-0705-0nbhpj2.json",
"Act.EduInst_hierarchy-spectral_20140713-0949-0m76br6.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_decreasing_20140417-2147-0m7g6cl.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-3z6kdki.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140417-2147-0m7g6cl.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-3z6kdki.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0202-43m4eba.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_random_20140309-0202-43m4eba.json",
"Arch.Struct_hierarchy-spectral_20140329-1845-42iib6o.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_decreasing_20140417-2147-0hrpu4q.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-42ih2wf.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140417-2147-0hrpu4q.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-42ih2wf.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_random_20140417-2147-43mfa1l.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_random_20140417-2147-43mfa1l.json",
"E.NP.WW_hierarchy-spectral_20140329-1845-05k6gq3.json",
"Event_hierarchy-entity-cobweb-partitioning_decreasing_20140309-0128-3z6ad5i.json",
"Event_hierarchy-entity-cobweb-partitioning_increasing_20140329-2044-014ed20.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0128-3z6ad5i.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2044-014ed20.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0225-0m7jilf.json",
"Event_hierarchy-entity-cobweb-partitioning_random_20140309-0225-0m7jilf.json",
"Event_hierarchy-spectral_20140329-1843-0m7igmx.json",
"Infr._hierarchy-entity-cobweb-partitioning_decreasing_20140309-0129-42ig0i5.json",
"Infr._hierarchy-entity-cobweb-partitioning_increasing_20140329-2050-3y2oswr.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0129-42ig0i5.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2050-3y2oswr.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_random_20140406-1132-04ga789.json",
"Infr._hierarchy-entity-cobweb-partitioning_random_20140406-1132-04ga789.json",
"Infr._hierarchy-spectral_20140329-1844-43m363w.json",
"Route_hierarchy-entity-cobweb-partitioning_decreasing_20140309-0158-4lde8l4.json",
"Route_hierarchy-entity-cobweb-partitioning_increasing_20140329-2038-4ftmp6v.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0158-4lde8l4.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2038-4ftmp6v.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0232-000chke.json",
"Route_hierarchy-entity-cobweb-partitioning_random_20140309-0232-000chke.json",
"Route_hierarchy-spectral_20140329-1844-0m7k7se.json",
"Species_hierarchy-entity-cobweb-partitioning_decreasing_20140419-1021-0ivma65.json",
"Species_hierarchy-entity-cobweb-partitioning_increasing_20140329-2038-0nbhpn3.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140419-1021-0ivma65.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2038-0nbhpn3.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_random_20140419-1413-4gxl2xc.json",
"Species_hierarchy-entity-cobweb-partitioning_random_20140419-1413-4gxl2xc.json",
"Species_hierarchy-spectral_20140329-1846-0140ukb.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_decreasing_20140309-1808-0005g03.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-0hrq6ju.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-1808-0005g03.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-0hrq6ju.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-1817-000gojq.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_random_20140309-1817-000gojq.json",
"Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json"]


dataset_db_map=dict()

dataset_db_map["Act."]=1
dataset_db_map["Arch"]=2
dataset_db_map["E.NP"]=3
dataset_db_map["Even"]=4
dataset_db_map["Infr"]=5
dataset_db_map["Rout"]=6
dataset_db_map["Spec"]=7
dataset_db_map["Tunn"]=8
from bisect import bisect_left

nodenumi=0

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def countone(e,a):
    if binary_search(e_a,str(e)+'*'+str(a))==-1:
        return 0
    else :
        return 1
    
def getValue(e,a):
    if countone(e,a)==1:
        return r.get(e_l[str(e)]+"|"+a_l[str(a)])

def countnode(root):
    global nodecount;
    nodecount=nodecount+1
    for c in root['children']:
        countnode(c)

def chooseAttrAtOneNode(node,entities):
    attributes=node['attributes']
    countatt=[None]*len(attributes)
    for  i,a in  enumerate(attributes) :
        sum=0
        for e in entities:
            sum=sum+countone(e,a)
        countatt[i]=[sum,a]
    countatt.sort(cmp=lambda x,y : cmp(x[0], y[0]),key=None,reverse=True)
    countattTop5=countatt[0:5]
    showattr=[]
    att_label=[]
    for v in countattTop5:
        showattr.append(v[1]) 
        att_label.append(a_l[str(v[1])])
    node['att_label']=att_label
    node['showattr']=showattr

def chooseatts(node):
    if len(node['children'])==0:
        chooseAttrAtOneNode(node,node['entities'])
        return node['entities']
    else:
        entities=[]
        for c in node['children']:
            entities=entities+chooseatts(c)
        chooseAttrAtOneNode(node,entities)
        return entities

def chooseEntitiesOneNode(node,entities,attibutes):
    countentities=[None]*len(entities)
    for i,e in enumerate(entities):
        sum=0
        for  a in  attibutes :
            sum=sum+countone(e,a)
        countentities[i]=[sum,e]
    countentities.sort(cmp=lambda x,y : cmp(x[0], y[0]),key=None,reverse=True)
    countentitiesTop5=countentities[0:5]
    showentities=[]
    entities_lable=[]
    for v in countentitiesTop5:
        showentities.append(v[1])
        entities_lable.append(e_l[str(v[1])])
    node['entities_lable']=entities_lable
    node['showentities']=showentities

def chooseEntities(node,pushedAtts):
    attributes=pushedAtts+node['showattr']
    if len(node['children'])==0:
        chooseEntitiesOneNode(node,node['entities'],attributes)
        return node['showentities']
    else:
        entities=[]
        for c in node['children']:
            entities=entities+chooseEntities(c,attributes)
        chooseEntitiesOneNode(node,entities,attributes)
        return entities


def createTableOneNode(node):
    e_a_v_table=[]  
    for e in node['showentities']:
        e_all_attr=[]
        for a in node['showattr']:
            attValue=getValue(e,a)
            e_all_attr.append(attValue)
        e_a_v_table.append(e_all_attr)
    node['table']=e_a_v_table

def createTable(node):
    createTableOneNode(node)
    for c in node['children']:
        createTable(c)
    
    
    
    
for filename in filenames:
    try:
        filename.index('spectral');
    except:
        continue
    nodenumi=0
    print 'loading json tree:',filename
    tree = json.loads(open(basedir+filename).read())
    
    
    r=redis.StrictRedis(host='127.0.0.1', port=6379, db=dataset_db_map[filename[0:4]])
    e_a_p=tree['entity-attribute']
    entity_labels_p=tree['entity_labels']
    attribute_labels_p=tree['attribute_labels']
    e_a=[]
    
     
    e_l=dict()
    for e_l_p in entity_labels_p:
        e_l[str(e_l_p['id'])]=e_l_p['label']
      
    
    a_l=dict()
    for   a_l_p in attribute_labels_p:
        a_l[str(a_l_p['id'])]=a_l_p['label']
      
 
    for v in e_a_p:
        e_a.append(str(v['entity'])+'*'+str(v['attribute']))
    e_a.sort()
    
    nodecount=0
    countnode(tree['root'])   
    print "Has ",nodecount," nodes"
       
    root=tree['root']  
 
    chooseatts(root)
    chooseEntities(root,[])
    createTable(root)
    
    
    
    def dropuseless(root):
        root.pop("entities", None)
        root.pop("attributes", None)
        for c in root['children']:
            dropuseless(c)
    print 'dropping  useless'
    dropuseless(root)
    f=open('/var/www/html/'+filename,'w')
    print 'Printing result'
    print >>f,json.dumps(root) 
    f.close()
    print filename, "    OVER\n"
    
    

print 'All OVER'








