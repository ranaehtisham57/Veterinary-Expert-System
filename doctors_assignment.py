import pandas as pd

class Doctor():
    def __init__(self):
        self.recommended_doctors={}
    def recommend_doctor(self,loc,price):
            if price==0:
                print("Price Cant be Zero")
                return {}

            self.recommended_doctors={}
            data=pd.read_csv(r"Expert Sys\doctors.csv")

            for (index,row) in data.iterrows():
                loc_match=0.5
                if row["Fee"]<=price:
                    budget_match=1
                else:
                    budget_match = max(0, 1 - ((row["Fee"] - price) / price))
                if loc.lower().strip() in row["City"].lower().strip():
                    loc_match=1
                score=(loc_match*50)+(budget_match*50)
                self.recommended_doctors[row["DoctorID"]]=[
                    row["Name"],
                    row["City"],
                    row["Specialty"],
                    row["Fee"],
                    row["Contact"],
                    row["Email"],
                    score
                ]
            
            if not self.recommended_doctors:
                return {}
            sorted_doctors = sorted(self.recommended_doctors.items(), key=lambda x: x[1][-1], reverse=True)

            return dict(sorted_doctors[:5])


def create_object():
    return Doctor()


if __name__=="__main__":
   pass