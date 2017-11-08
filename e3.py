import pandas as pd

tasks={
    "Alleghany County":"alleghany_county.pdf",
    "Alexandria City":"alexandria_city.pdf",
    "Albemarle County":"albemarle_county.pdf",
    "Accomack County":"accomack_county.pdf"}

for area in tasks:
    
    years=[]
    shares=[]
    
    with open("ELECTION_ID", "r") as input:
        rows=input.read().split('\n')
        for row in rows:
            year=row.split(' ')[0]
            
            header=pd.read_csv("president_general_" + year + ".csv", nrows=1).dropna(axis=1)
            d=header.iloc[0].to_dict()
            df=pd.read_csv("president_general_" + year + ".csv", index_col=0, thousands=",", skiprows=[1])
            
            df.rename(inplace=True, columns=d)
            df.dropna(inplace=True, axis=1)
            
            if area not in df.index:
                continue
                
            record = df.loc[area]
            years.append(int(year))
            shares.append(record["Republican"] / record["Total Votes Cast"])
    
    years.reverse()
    shares.reverse()
    df=pd.DataFrame({"Year":years, "Share of Replican":shares})
    df.plot(x="Year", y="Share of Replican").figure.savefig(tasks[area])
    