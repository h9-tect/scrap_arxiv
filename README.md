# Python code can scrap arxiv web site and put them on csv file 

### git clone https://github.com/h9-tect/scrap_arxiv.git

### cd scrap_arxiv

### pip install .

## sample usage 
paper = Paper(from_="2022-05-020",
              to_="2022-05-26",
              set_="cs",
             )

## Get today's papers

paper = Paper()
arxiv = arXiv(paper)
