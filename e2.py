import requests

with open("ELECTION_ID", "r") as input:
    text=input.read()
    rows=text.split('\n')
    for row in rows:
        cols=row.split(' ')
        year=cols[0]
        link=cols[1]
        
        with open('president_general_'+year+'.csv','w') as output:
            r=requests.get('http://historical.elections.virginia.gov/elections/download/'+link+'/precincts_include:0/')
            csv=r.text
            output.write(csv)