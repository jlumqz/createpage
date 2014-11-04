#encoding=utf-8
htmltmp_1='''
<!DOCTYPE html>
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

var margin = {top: 40, right: 120, bottom: 20, left: 120},
    width = 9600 - margin.right - margin.left,
    height = 500 - margin.top - margin.bottom;
    
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


htmltmp_2='''", function(error, data) {  
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
        title=title+'<th width=150 style="word-wrap:break-word;word-break:break-all;">'+d.att_label[i]+'</th>';
     page=page+title+'<tr>';

     content='';
 
    for (i=0;i<d.table.length ;i++ )
    {
        onerow='<tr> <td width=150 style="word-wrap:break-word;word-break:break-all;"> '+d.entities_lable[i]+'</td>'
        for(j=0;j<d.att_label.length;j++)
        {
            onerow=onerow+'<td width=150 style="word-wrap:break-word;word-break:break-all;">'+d.table[i][j]+'</td>';
        }
        onerow=onerow+'</tr>';
        content=content+onerow;
    //    alert(onerow)
    }
    page=page+content+'</table> '
    //alert(title);
    // alert(d.att_label[0]);
      
     
    //    d3.select(this.parentNode).append('g').append("text").text('adfasdfads');
         
d3.select(this.parentNode).append("foreignObject")
    .attr("width", 3000)
    .attr("height", 2000)
  .append("xhtml:body")
    .style("font", "14px 'Helvetica Neue'")
    .html(page);
     
 
      })
      .on('mouseout', function(d){
      
 
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
filenames=os.listdir('/var/www/html/')

basedir='/var/www/html/'

findex=open(basedir+'index.html','w')

for filename in filenames:
    if filename.endswith('.json') == False:
        continue
    print >>findex,'<a target="_blank" href="'+filename+'.html">'+filename+'.html</a><br/>'
    
    fout=open(basedir+filename+'.html','w')
    print >>fout,htmltmp_1,
    print >>fout,filename,
    print >>fout,htmltmp_2
    fout.close()
    
findex.close()


print 'OVER'






