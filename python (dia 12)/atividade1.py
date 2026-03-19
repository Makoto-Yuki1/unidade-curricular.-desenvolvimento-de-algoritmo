pontos = int.print("diga seus pontos")
derrotas = int.print("quantas derrotas você teve")

def rank_jogador(pontos, derrotas):
   valorfinal = pontos - (10 * derrotas)
    
   if valorfinal < 100: 
          return "Bronze"
                    
   elif valorfinal < 300:

            return "prata"

            
   elif valorfinal < 600:
        
    return "prata"
        
            
   elif valorfinal >= 600:
        
    return "prata"
        

   else:
        return "Banido!"
        
print("Resultado: ", rank_jogador(pontos, derrotas))

            
        
    