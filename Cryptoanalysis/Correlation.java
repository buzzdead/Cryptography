import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Correlation
{   
	
	public static int[][] vRs = new int[42][42];
	public static int[][] vRs2 = new int[42][42];
	
	// Array with values given in main, the values in this are the weight of the vector.
	public static int[] vecto = new int[vRs.length];
	
	// Used for A^i , method called matrixPow
	public static double m = 2;
	public static int[][] m2 = new int[41][41];
    
    // Resets the helper array for powering a matrix A^i.
    public static void resetM2() {
    	for(int i=0; i<41; i++) {
    	 for(int j=0; j<41; j++) {
    		 m2[i][j]=0;
    	 
    	 }
    	}
    }
 
    
    // Powering matrices. m1 is the original one, m2 is the new one, m3 is the helper one in the function:
    // So recursively: A^5 = A^4*A and so on.
    public static void matrixPow(int[][] m1, double n) {
    	if(m>n) return;
    	else if(m==2) {
    		resetM2();
    		for(int i=0; i<41; i++) {
    			for(int j=0; j<41; j++) {
    				for(int l=0; l<41; l++) {
    					m2[i][j]+=(m1[i][l]*m1[l][j]);
    			}
    		}
    		}
    	
    } else if(m<=n) { int[][] m3 = new int[41][41];
	for(int i=0; i<41; i++) {
		for(int j=0; j<41; j++) {
			m3[i][j] = m2[i][j];
		}
	}
	resetM2();
	
	for(int i=0; i<41; i++) {
		for(int j=0; j<41; j++) {
			for(int l=0; l<41; l++) {
				m2[i][j]+=(m3[i][l]*m1[l][j]);
			}
			m2[i][j]=m2[i][j]%2;
		}
	}
    }
    	m++;
    	matrixPow(m1,n);
    	
    }
    // Method I use after designating a 
    public static void rowReduce(int pivot,int pivotPos, int[][] vRs, ArrayList<Integer> pivotL) {
    	for(int i=0; i<vRs.length; i++) {
    		
    		
    		if(!pivotL.contains(i) && vRs[i][pivotPos]==1) {

    		for(int j=0; j<42; j++) {
    		vRs[i][j]=vRs[i][j]^vRs[pivot][j];
    		
    		}vecto[i]=vecto[i]^vecto[pivot];
    		}
    } 
    }
    
    public static void clearr(int[] row) {
    	for(int i=0; i<row.length; i++) {
    		row[i]=0;
    	}
    		
    }

    // Method for trying to scramble the array of vectors.
    public static void further(int w) {
    	int[] pivRow = new int[vRs.length];
    	for(int i=vRs.length-1; i>0; i--) {
    		clearr(pivRow);
    		int counter2 = 0;
    		for(int j=0; j<42; j++) {
    			pivRow[j]=vRs[i][j];
    			if(pivRow[j]==1)
    			counter2++;
    		}
    			
    			for(int a=i-1; a>=0; a--) {
    				
    			int counter = 0;
    				for(int b=0; b<42; b++) {
    					if(vRs[a][b]==pivRow[b] && pivRow[b]==1) {
    						counter++;
    					}
    				}
    					if(counter2-counter<w) {
    						for(int r=0; r<42; r++) {
    							vRs[a][r]=vRs[a][r]^pivRow[r];
    						}
    						
    						vecto[a]=vecto[a]^vecto[i];
    					}
    				}
    			}
    			
    		}
    // Same method from top to bottom.
    public static void furtherR(int w) {
    	int[] pivRow = new int[vRs.length];
    	for(int i=0; i<vRs.length-1; i++) {
    		clearr(pivRow);
    		int counter2 = 0;
    		for(int j=0; j<42; j++) {
    			pivRow[j]=vRs[i][j];
    			if(pivRow[j]==1)
    			counter2++;
    		}
    			
    			for(int a=i+1; a<42; a++) {
    				
    			int counter = 0;
    				for(int b=0; b<42; b++) {
    					if(vRs[a][b]==pivRow[b] && pivRow[b]==1) {
    						counter++;
    					}
    				}
    					if(counter2-counter<w) {
    						for(int r=0; r<42; r++) {
    							vRs[a][r]=vRs[a][r]^pivRow[r];
    						}
    						vecto[a]=vecto[a]^vecto[i];
    					}
    				}
    			}
    			
    		}
    	
    
    	
    
    
    // a huge chunk of spaghetti code. But it should all be in place.
    public static void main(String args[]) 
    { 
    	int[] an = {0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};
    	int[] hk = new int[180];
    	int[] mk = new int[180];
    	int[][] m1 = new int[41][41];
    	for(int i=0; i<40; i++) {
    		m1[i][i+1]=1;
    	}
    	m1[37][0]=1;
    	m1[40][0]=1;
    	
    	
    	int[] vec1 = new int[41];
    	for(int i=0; i<41; i++) {
    		vec1[i]=0;
    	}
    		vec1[0]=1;
    		vec1[35]=1;
    		vec1[34]=1;
    	
    	double[][] vector = new double[vRs.length][2];
    	int[] keyStream = {1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0};
    	int a=41; int b=3; int c = 0;
    	for(int i = 0; i<180-a; i++) {
    		mk[a]++; mk[b]++; mk[c]++; 
    		if(a<180) {
    			if((keyStream[a]^keyStream[b]^keyStream[c])==0) {
    				hk[a]++; hk[b]++; hk[c]++; 
    			}
    			a+=1; b+=1; c+=1;
    		}
    	}
    	a=82; b=6; c=0;
    	for(int i = 0; i<180-a; i++) {
    		mk[a]++; mk[b]++; mk[c]++; 
    		if(a<180) {
    			if((keyStream[a]^keyStream[b]^keyStream[c])==0) {
    				hk[a]++; hk[b]++; hk[c]++; 
    			}
    			a+=1; b+=1; c+=1;
    		}
    	}
    	a = 164; b=12; c=0;
    	for(int i = 0; i<180-a; i++) {
    		mk[a]++; mk[b]++; mk[c]++; 
    		if(a<180) {
    			if((keyStream[a]^keyStream[b]^keyStream[c])==0) {
    				hk[a]++; hk[b]++; hk[c]++; 
    			}
    			a+=1; b+=1; c+=1;
    		}
    	}
    	double p = 0.75; double s = p*p+(1-p)*(1-p);
    	int k = 0;
    	for(int i=0; i<180; i++) {
    		
    		double d = p*Math.pow(s, hk[i])*Math.pow((1-s),mk[i]-hk[i]);
    		double e = d+(1-p)*Math.pow((1-s), hk[i])*Math.pow(s, (mk[i]-hk[i]));
    			if(d/e!=0) {
    				if(k<vRs.length) {
    					vector[k][0] = (d/e);
    					vector[k][1] = i;
    					k++;
    				}
    				else {
    			for(int j =0; j<vRs.length; j++) {
    				if((d/e)>vector[j][0]) {vector[j][0] = (d/e);
    				vector[j][1] = i;
    				break;
    				}
    			}
    		    		
    	}
    	}
    	}
      
    	
    	System.out.println("Printing probabilities Pk");
    	Arrays.sort(vector, new Comparator<double[]>() {      
            @Override
            public int compare(double[] o1, double[] o2) {
                return Double.compare(o2[1], o1[1]);
            }
        });
    	
    	for(int i = 0; i<vRs.length; i++) {
    		System.out.println(vector[i][0] + ", Pos:" + vector[i][1]);
    	}
    	System.out.println();
    	int[] sv = new int[41];
    	
    	for(int i=0; i<42; i++) {
    		for(int j=0; j<42; j++) {
    			vRs[i][j]=0;
    		}
    	}
    	System.out.println("Printing Vector");
        for(int q=vRs.length-1; q>=0; q--) {
        	int n = 0;
        	m=2;
        	resetM2();
        	for(int i=0; i<41; i++) {
        		sv[i]=0;
        	}
        	matrixPow(m1,vector[q][1]);
        	for(int i=0; i<41; i++) {
        		
        		for(int j=0; j<41; j++) {
        				sv[40-i]+=m2[i][j]*an[j];
        			}
        		sv[40-i] = sv[40-i]%2;
        		if(sv[40-i]!=0) {
        			
        		
        		int y = 40-i;
        		int ab = vRs.length-1-q;
        		vRs[ab][y]=1;
        		n=n^keyStream[y];
        		System.out.print("s" + y);
        		} 
        	} 
        	System.out.println(" u" + vector[q][1]);
        	vRs[vRs.length-1-q][41]=n;
 
        }
        
        System.out.println("\nPrinting states s40,....,0, last two digits is the +1\0 and vector weight");
        for(int i=0; i<vRs.length; i++) {
        	for(int j=0; j<42; j++) {
        		System.out.print(vRs[i][j]);
        	}
        	System.out.println();
        }
        System.out.println();
        for(int i=0; i<vRs.length; i++) {
        	vecto[i]=0;
        }
        
      

        ArrayList<Integer> pivotL = new ArrayList<Integer>();
        int pivot =0;
        int pivotPos = 0;
        int the = 0;
        for(int i=0; i<42; i++) {
        for(int j=0; j<vRs.length; j++) {
        	if(vRs[j][i]==1 && !pivotL.contains(j)) { pivot = j; pivotL.add(j); pivotPos = i;
        	
        		for(int u=0; u<42; u++) {
        		vRs2[the][u]=vRs[pivot][u];
        	
        	}
        		the++;
        	rowReduce(pivot,pivotPos,vRs,pivotL);
      
        	break;
        	}
        }
        }


       
        for(int i=0; i<vRs.length; i++) {
        	for(int j=0; j<42; j++) {
        		int y = 41-j-1;
        		if(vRs[i][j]==1 && j<41) System.out.print("s"+y+ "  ");
        		else System.out.print(vRs[i][j]+"  ");
        	}
        	System.out.print(" " + vecto[i]);
        	System.out.println();
        }
        
      
        	
        }
}
