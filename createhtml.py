#encoding=utf-8
htmltmp_1='''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">

    <title>Collapsible Tree Example</title>
<style>

table, th, td {
    border: 2px solid steelblue;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;
    background-color: rgb(255,255,255);
}
table th    {
    background-color: steelblue;
}
</style>
 

    <style>

    .node circle {
      fill: #fff;
      stroke: steelblue;
      stroke-width: 3px;
    }

    .node text { font: 12px sans-serif; }

    .link {
      fill: none;
      stroke: #ccc;
      stroke-width: 2px;
    }
    
    </style>

  </head>

  <body>

<!-- load the d3.js library -->    
<script src="http://d3js.org/d3.v3.min.js"></script>
    
<script>
var mouse = {x: 0, y: 0};

document.addEventListener('mousemove', function(e){ 
    mouse.x = e.clientX || e.pageX; 
    mouse.y = e.clientY || e.pageY 
}, false);
var margin = {top: 40, right: 120, bottom: 20, left: 120},
    width = 9600 - margin.right - margin.left,
    height = '''
    
    
    
htmltmp_2='''- margin.top - margin.bottom;
    
var i = 0;

var tree = d3.layout.tree()
    .size([height, width]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.x, d.y]; });

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
    var root ;
d3.json("'''


htmltmp_3='''", function(error, data) {  
 if(error)
 {
 console.log(error);
 }
 else
 {

root=data;
update(root);
}
});

function update(source) {

 // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
      links = tree.links(nodes);
 
  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 100; });

  var node = svg.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });
 
  // Enter the nodes.
  var nodeEnter = node.enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { 
          return "translate(" + d.x + "," + d.y + ")"; });
 
  nodeEnter.append("circle")
      .attr("r", 10)
      .style("fill", "#fff")
      .on('mouseover',function(d){
        //   alert(d.att_label.length);
     var i=0;
     var page='  <table   border="1"   >  <tr><th width=150 style="word-wrap:break-word;word-break:break-all;"></th>';
     title='';
     for(i=0;i<d.att_label.length;i++)
        title=title+'<th width=100 style="word-wrap:break-word;word-break:break-all;">'+d.att_label[i]+'</th>';
     page=page+title+'<tr>';

     content='';
 
    for (i=0;i<d.table.length ;i++ )
    {
        onerow='<tr> <td width=150 style="word-wrap:break-word;word-break:break-all;"> '+d.entities_lable[i]+'</td>'
        for(j=0;j<d.att_label.length;j++)
        {
            onerow=onerow+'<td width=100 style="word-wrap:break-word;word-break:break-all;">'+d.table[i][j]+'</td>';
        }
        onerow=onerow+'</tr>';
        content=content+onerow;
    }
    page=page+content+'</table> '
    screenheight=window.screen.height;
    screenwidth=window.screen.width;
    
    shiftx=d.x+750-screenwidth+10;
   shifty=d.y+500-screenheight+10;
  if(shiftx<0)
      shiftx=0;
  if(shifty<0)
      shifty=0;
   rx= shiftx;
    ry= shifty; 


            d3.select(this.parentNode).append("foreignObject")
                .attr("width", 3000)
                .attr("height", 2000)
              .append("xhtml:body")
              .style("font", "14px 'Helvetica Neue'")
          //    .style("position", "absolute")
            //  .style("left",300)
             // .style("top",300)
              .html(page);
              
              
  }).on('mouseout', function(d){
      
 
        d3.select(this.parentNode).selectAll(function() { return this.getElementsByTagName("foreignObject"); }).remove();

      
      })
      ;
 
  nodeEnter.append("text")
      .attr("y", function(d) { 
          return d.children || d._children ? -18 : 18; })
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(function(d) { return d.name; })
      .style("fill-opacity", 1);
  var link = svg.selectAll("path.link")
      .data(links, function(d) { return d.target.id; });
 
  // Enter the links.
  link.enter().insert("path", "g")
      .attr("class", "link")
      .attr("d", diagonal);
 
}

</script>
    
  </body>
</html>

'''



import os
filenames_height={
            'Act.EduInst_hierarchy-spectral_20140713-0949-0m76br6.json':1000,
            'Arch.Struct_hierarchy-spectral_20140329-1845-42iib6o.json':2000,
            'E.NP.WW_hierarchy-spectral_20140329-1845-05k6gq3.json':2000,
            'Event_hierarchy-spectral_20140329-1843-0m7igmx.json':1000,
            'Infr._hierarchy-spectral_20140329-1844-43m363w.json':2000,
            'Route_hierarchy-spectral_20140329-1844-0m7k7se.json':1000,
            'Species_hierarchy-spectral_20140329-1846-0140ukb.json':600,
            'Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json':500,
           }


basedir='/var/www/html/'

findex=open(basedir+'index.html','w')

for (filename,height) in  filenames_height.items(): 
    print filename,height
    if filename.endswith('.json') == False:
        continue
    print >>findex,'<a target="_blank" href="'+filename+'.html">'+filename+'.html</a><br/>'
    
    fout=open(basedir+filename+'.html','w')
    print >>fout,htmltmp_1,
    print >>fout,height,
    print >>fout,htmltmp_2,
    print >>fout,filename,
    print >>fout,htmltmp_3
    fout.close()

print >>findex,''
findex.close()


print 'OVER'






