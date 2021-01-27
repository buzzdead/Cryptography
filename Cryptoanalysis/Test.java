
public class Test {
	public static double m = 2;
	
	  public static void matrixPow(int[][] m1, double n) {
	    	if(m>n) return;
	    	if(m==2) {
	    		for(int i=0; i<4; i++) {
	    			for(int j=0; j<4; j++) {
	    				for(int l=0; l<4; l++) {
	    					m2[i][j]+=(m1[i][l]*m1[l][j]);
	    			}
	    		}
	    		}
	    	
	    } else if(m<=n && m>2) { int[][] m3 = new int[4][4];
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				m3[i][j] = m2[i][j];
			}
		}
		resetM2();
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				for(int l=0; l<4; l++) {
					m2[i][j]+=(m3[i][l]*m1[l][j]);
				}
				m2[i][j]=m2[i][j]%2;
			}
		}
	    }
	    	m++;
	    	matrixPow(m1,n);
	    	
	    }
	  
	  public static void resetM2() {
	    	for(int i=0; i<4; i++) {
	    	 for(int j=0; j<4; j++) {
	    		 m2[i][j]=0;
	    	 
	    	 }
	    	}
	    	
	    }
	
	public static int[][] m2 = new int[4][4];

	public static void main(String[] args) {
		double p = 0.75;
        double s = p*p+(1-p)*(1-p);
        double[] hk = {1,2,4,4,2,3,3,2,1,2,2,1};
        double[] mk = {2,3,4,4,4,4,3,3,3,2,2,2};
        System.out.println("Calculating pk...");
        for(int i = 0; i<12; i++) {
        
        	
        double d = p*Math.pow(s, hk[i])*Math.pow((1-s),mk[i]-hk[i]);
		double e = d+(1-p)*Math.pow((1-s), hk[i])*Math.pow(s, (mk[i]-hk[i]));

		System.out.println(d/e);
        }
		int[] vector = {2,3,5,6,10};
	
		int[][] m1 = new int[4][4];
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				m1[i][j]=0;
			}
		}
		m1[0][1]=1;m1[1][2]=1;m1[2][0]=1; m1[2][3]=1;m1[3][0]=1;
		

	   int[] vec = new int[4];
	   for(int i=0; i<4; i++) {
		   vec[i]=0;
	   }
	   vec[1]=1;
	   int[] sv = new int[4];
//	   matrixPow(m1,6);
//	   for(int i=0; i<4; i++) {
//		   for(int j=0; j<4; j++) {
//			   System.out.print(m2[i][j]);
//		   }
//		   System.out.println();
//	   
	   System.out.println("\nTesting power of matrix");
	   for(int q=0; q<5; q++) {
      	int n = 0;
       	m=2;
      	resetM2();
       	for(int i=0; i<4; i++) {
      		sv[i]=0;
      	}       	matrixPow(m1,vector[q]);
       	for(int i=0; i<4; i++) {
      		n=0;
       		for(int j=0; j<4; j++) {
       				sv[3-i]+=m2[i][j]*vec[j];
       			}
     		sv[3-i] = sv[3-i]%2;
       		if(sv[3-i]!=0) {
      			
      		
      		int y = 3-i;
      		System.out.print("s" + y);
       		}
      		
      	} System.out.println();
	   
//	for(int i=0; i<4; i++) {
//		for(int j=0; j<4; j++) {
//		System.out.print(m1[i][j]);
//	}
//	System.out.println();


	}
}
	}


