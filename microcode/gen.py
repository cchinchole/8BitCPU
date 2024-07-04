from array import array

ALLOFF   =  0b000000000000000000000000

CTRLMSK  =  0b000000000000000011110000 # 0 for active high 1 for active low
PCE      =  0b100000000000000000000000 # [ Program Counter Enable (No Bus)       ] Active High
PCL      =  0b010000000000000000000000 # [ Load Program Counter   (Data Bus)     ] Active High 
PCO      =  0b001000000000000000000000 # [ Program Counter Out    (Address Bus)  ] Active High
WRA      =  0b000100000000000000000000 # [ Write To Ram           (Data Bus)     ] Active High (AND clk) 
LI       =  0b000010000000000000000000 # [ Load Instruction Reg   (Data Bus)     ] Active High (AND clk)
ADE      =  0b000001000000000000000000 # [ Addr Register Enab     (No Bus)       ] Active High
ADL      =  0b000000100000000000000000 # [ Addr Register Load     (Data Bus)     ] Active High 
ADO      =  0b000000010000000000000000 # [ Addr Register Out      (Address Bus)  ] Active High

C08      =  0b000000001000000000000000 # NOT CONNECTED 
BRI      =  0b000000000100000000000000 # [ B Register Load        (Data Bus)     ] Active High (AND clk)
ES       =  0b000000000010000000000000 # [ Enable Subtraction     (No Bus)       ] Active High 
EC       =  0b000000000001000000000000 # [ Enable Carry           (No Bus)       ] Active High
HILO     =  0b000000000000100000000000 # [ HIGH / LOW Program Ctr (No Bus)       ] Active High
RC       =  0b000000000000010000000000 # [ Reset Ring Counter     (No Bus)       ] Active High 
TX       =  0b000000000000001000000000 # [ Transmit Data          (Data Bus)     ] Active High
RX       =  0b000000000000000100000000 # [ Recieve Data           (Data Bus)     ] Active High

AO       =  0b000000000000000010000000 # [ Output A Register      (Data Bus)     ] Active Low               
BO       =  0b000000000000000001000000 # [ Output B Register      (Data Bus)     ] Active Low
ALO      =  0b000000000000000000100000 # [ Output ALU             (Data Bus)     ] Active Low
RO       =  0b000000000000000000010000 # [ Output Ram             (Data Bus)     ] Active Low
ACL0     =  0b000000000000000000001000 # [ A Select line 0        (Data Bus)     ] 3- LOAD Data 2- Shift Right 1- Shift Left 0- Hold Data 
ACL1     =  0b000000000000000000000100 # [ A Select line 1        (Data Bus)     ] 3- LOAD Data 2- Shift Right 1- Shift Left 0- Hold Data
C22      =  0b000000000000000000000010 # NOT CONNECTED
C23      =  0b000000000000000000000001 # NOT CONNECTED

FETCH = PCE|PCO|RO|LI
LOADA = ACL0|ACL1  # 3
SHIFTLEFTA = ACL1  # 2
SHIFTRIGHTA = ACL0 # 1

NOP = [FETCH, RC,       0,             0,     0,      0, 0, 0]
LDI = [FETCH, PCO|PCE|RO|LOADA, RC,    0,     0,      0, 0, 0]
LDA = [FETCH, PCE|PCO|RO|ADL, PCO|RO|HILO|ADL, RO|LOADA|PCE|ADO, RC, 0, 0, 0]
JMP = [FETCH, PCE|PCO|RO|BRI, PCL|PCO|RO|HILO,      BO|PCL, RC,   0, 0, 0]
ADD = [FETCH, PCO|PCE|RO|BRI, ALO|LOADA, RC, 0, 0, 0, 0]
STA = [FETCH, PCE|PCO|RO|ADL, PCO|RO|HILO|ADL, WRA|AO|PCE|ADO, RC, 0, 0, 0]
SHR = [FETCH, PCE|SHIFTRIGHTA, RC, 0, 0, 0, 0, 0]
SHL = [FETCH, PCE|SHIFTLEFTA,  RC, 0, 0, 0, 0, 0]

myarray = [
      NOP,                      # 0000 0000 - 0x0000  - NOP
      LDI,                      # 0000 0001 - 0x0001  - LDI
      LDA,                      # 0000 0010 - 0x0002  - LDA
      ADD,                      # 0000 0011 - 0x0003  - ADD
      STA,                      # 0000 0100 - 0x0004  - STA
      JMP,                      # 0000 0101 - 0x0005  - JMP 
      NOP,                      # 0000 0110 - 0x0006  - 
      NOP,                      # 0000 0111 - 0x0007  - 
      NOP,                      # 0000 1000 - 0x0008  - 
      NOP,                      # 0000 1001 - 0x0009  - 
      NOP,                      # 0000 1010 - 0x000A  - 
      NOP,                      # 0000 1011 - 0x000B  - 
      NOP,                      # 0000 1100 - 0x000C
      NOP,                      # 0000 1101 - 0x000D
      NOP,                      # 0000 1110 - 0x000E
      NOP,                      # 0000 1111 - 0x000F
      NOP,                      # 0001 0000 - 0x0010
      NOP,                      # 0001 0001 - 0x0020
      NOP,                      # 0001 0010 - 0x0030
      NOP,                      # 0001 0011 - 0x0040
      NOP,                      # 0001 0100 - 0x0050
      NOP,                      # 0001 0101 - 0x0060
      NOP,                      # 0001 1000 - 0x0070
      NOP,                      # 0001 1000 - 0x0080
      NOP,                      # 0001 1001 - 0x0090
      NOP,                      # 0001 1010 - 0x00A0
      NOP,                      # 0001 1011 - 0x00B0
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP, # 1111 1111
      #255 - 512
      NOP,                     
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                         
      NOP,                         
      NOP,                        
      NOP,                        
      NOP,                        
      NOP,                       
      NOP,                      
      NOP,                        
      NOP,                        
      NOP,                         
      NOP,                         
      NOP,                         
      NOP,                     
      NOP,                      
      NOP,                   
      NOP,                  
      NOP,     
      NOP,      
      NOP,                    
      NOP,                    
      NOP,                      
      NOP,                      
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,

      
      #255 - 512
      NOP,                     
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                         
      NOP,                         
      NOP,                        
      NOP,                        
      NOP,                        
      NOP,                       
      NOP,                      
      NOP,                        
      NOP,                        
      NOP,                         
      NOP,                         
      NOP,                         
      NOP,                     
      NOP,                      
      NOP,                   
      NOP,                  
      NOP,     
      NOP,      
      NOP,                    
      NOP,                    
      NOP,                      
      NOP,                      
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,

      
      #255 - 512
      NOP,                     
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                      
      NOP,                         
      NOP,                         
      NOP,                        
      NOP,                        
      NOP,                        
      NOP,                       
      NOP,                      
      NOP,                        
      NOP,                        
      NOP,                         
      NOP,                         
      NOP,                         
      NOP,                     
      NOP,                      
      NOP,                   
      NOP,                  
      NOP,     
      NOP,      
      NOP,                    
      NOP,                    
      NOP,                      
      NOP,                      
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
      NOP,
]
binary_output = open('microcode_rom1.bin', 'wb')
binary_output2 = open('microcode_rom2.bin', 'wb')
binary_output3 = open('microcode_rom3.bin', 'wb')

w, h = 8, 1024

lowbytes = [[0 for x in range(w)] for y in range(h)]
midbytes = [[0 for x in range(w)] for y in range(h)]
highbytes = [[0 for x in range(w)] for y in range(h)]

for x in range(0, h):
    for y in range(0, w):
        print("Trying [ "+str(x)+" ] [ "+str(y)+" ]")
        lowbytes[x][y] = (( ((myarray[x][y] & 0b00000000000000000000000011111111)^CTRLMSK)              ))
        midbytes[x][y] = (( ((myarray[x][y] & 0b00000000000000001111111100000000)^CTRLMSK) >> 8         ))
        highbytes[x][y] = (( ((myarray[x][y] & 0b00000000111111110000000000000000)^CTRLMSK) >> 16        ))

for x in range(0, h):
       low = bytes( lowbytes[x] )
       mid = bytes( midbytes[x] )
       high = bytes( highbytes[x] )
       binary_output.write(high)
       binary_output2.write(mid)
       binary_output3.write(low)
       
binary_output.close()
binary_output2.close()
binary_output3.close()
