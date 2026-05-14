import pandas as pd
class Disease_diagnosis:
    def __init__(self):
        self.data=pd.read_csv(r"Expert Sys\disease_symptoms.csv")
        self.treatment=pd.read_csv(r"Expert Sys/treatments.csv")
        self.calculated_disease={}


    def calculate_score(self,symtoms):
        self.calculated_disease={}
        for user_symtom in symtoms:
            for index,row in self.data.iterrows():
                if row['Symptom'].lower().strip()==user_symtom.lower().strip():
                    disease=row["Disease"].lower().strip()

                    weight=row['Weight']
                    if  disease not in self.calculated_disease:
                        self.calculated_disease[disease]=weight
                    else:
                        self.calculated_disease[disease]+=weight

        if not self.calculated_disease:
            return {}
        sorted_diseases = sorted(self.calculated_disease.items(), key=lambda x: x[1], reverse=True)

        return dict(sorted_diseases[:3])

    def calculate_confidence(self,calculated_disease_dict):
        total=sum(calculated_disease_dict.values())
        if total==0:
            return {"status": "no_match", "confidence": 0}
        return {k:round((v/total)*100,2) for k,v in calculated_disease_dict.items()}
    
    def treatment_recommend(self,calculated_disease_dict):

        if not calculated_disease_dict:
            return {}


        sorted_diseases = sorted(calculated_disease_dict.items(), key=lambda x: x[1], reverse=True)
        high_disease=sorted_diseases[0][0].strip().lower()
        
        for index,row in self.treatment.iterrows():
            if row["Disease"].lower().strip()==high_disease:
                return {
                    "Disease":row["Disease"],
                    "Medicine":row["Medicine"],
                    "BrandName":row["BrandName"],
                    "Dosage":row["Dosage"],
                    "Duration":row["Duration"]
                }
        return {}




def create_object():
    return Disease_diagnosis()

if __name__=="__main__":
    pass

