import java.util.ArrayList;
import java.util.HashSet;



public class SPN {

	public static int[] w1 = new int[16];
	public static int[] s = {14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7};
	public static int[] p = {99,1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16}; 
	public static int[] y = new int[16];
	public static int[] nk = {1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0};
	public static int[] nk2 = {1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1};
	public static int[] nk3 = {1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0};
	public static int[] nk4 = {1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1};
    public static int[] x1 = {1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0};
    public static int[] x2 = {0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0};
    public static int[] x3 = {1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0};
    public static int[] x4 = {0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0};
    int[] k1 = new int[16];
    public static void main(String[] args) {
	ArrayList<HashSet<Integer>> lol = new ArrayList<HashSet<Integer>>();
double time1 = System.currentTimeMillis();
for(int i=0; i<4096; i++) {
	lol.add(new HashSet<Integer>());
}

for(int i=0; i<256; i++) {
	for(int j=0; j<4096; j++) {
		lol.get(j).add(encrypt(Binarize(i).substring(8, 16).concat(Binarize2(j).substring(20, 32)).concat("000000000000"),x3));
	}
}


int abc = 0;
for(int i=(int)Math.pow(2, 0); i<Math.pow(2, 24); i++) {
	if(lol.get(Integer.parseInt(Binarize2(i).substring(8, 20),2)).contains(decrypt2(Binarize2((i)),nk3))) {
	for(int j=0; j<Math.pow(2, 8); j++) { abc=0;
	String a = (Binarize(j).substring(8, 16).concat(Binarize2(i).substring(8, 32)));
		encrypt3(a,x3);
		encrypt2(a);
		for(int r=0; r<16; r++) {
			if(nk3[r]!=y[r]) {abc=1; break;}
		}
		if(abc==0) { encrypt3(a,x2);
		encrypt2(a);
		for(int r=0; r<16; r++) {
			if(nk2[r]!=y[r]) {abc=1; break;}
		}
		}
		if(abc==0) { encrypt3(a,x4);
		encrypt2(a);
		for(int r=0; r<16; r++) {
			if(nk4[r]!=y[r]) {abc=1; break;}
		}
		}
		if(abc==0) { System.out.println("The key must be: "+a);
		System.out.println("Testing for different pairs of plaintexts and ciphertexts... ");
		test(x1,nk,a);
		test(x2,nk2,a);
		test(x3,nk3,a);
		test(x4,nk4,a);
		}
	}
	}
}
double time2 = System.currentTimeMillis();
double time = time2-time1;
System.out.println("\nRuntime: " + time/1000/60 + " Minutes");
}
    
    public static void test(int[] x, int[] n, String a) {
    	System.out.print("\nTesting: ");
		for(int h=0; h<16; h++) System.out.print(x[h]+",");
		System.out.print("\nciphertext is supposed to be: ");
		for(int h=0; h<16; h++) System.out.print(n[h]+",");
		encrypt3(a,x);
		encrypt2(a);
		System.out.print("\nEncrypting..");
		System.out.print("\nCiphertext is: ");
		for(int h=0; h<16; h++) System.out.print(y[h]+",");
		System.out.println();
    }







 public static String Binarize(int i) {
String binarized = Integer.toBinaryString(i);
int len = binarized.length();
String sixteenZeroes = "00000000000000000";
if (len < 16)
  binarized = sixteenZeroes.substring(0, 16-len).concat(binarized);
else
  binarized = binarized.substring(len - 16);
return binarized;



}
 public static String Binarize2(int i) {
String binarized = Integer.toBinaryString(i);
int len = binarized.length();
String sixteenZeroes = "0000000000000000000000000000000000";
if (len < 32)
  binarized = sixteenZeroes.substring(0, 32-len).concat(binarized);
else
  binarized = binarized.substring(len - 32);
return binarized;



}
 
 public static String[] orgKey(String k) {
	 String[] KR = new String[5];
	 for(int i=0; i<5; i++) {
		 KR[i]="";
		 for(int j=0; j<16; j++) {
			 KR[i]+=k.charAt(4*(i+1)-4+j);
		 }
	 } return KR;
 }
 public static int encrypt(String k,int[] x) {
	 String[] abc = orgKey(k);
	 int a = 0;
	 int b = 0;
	 int[] w = new int[16];
	 for(int i=0; i<16;i++)w[i]=x[i];
	 int[] u = new int[16];
	 int[] v = new int[16];
	
	 
	 for(int i=0; i<2; i++) {
		 for(int j=0; j<16; j++) {
			 u[j]=(w[j]+abc[i].charAt(j))%2;
			 
		 }
		 for(int r=0; r<4; r++) {
			 a=0;
		 
		 for(int j=0; j<4; j++) {
			 a = a + (int)(Math.pow(2, 3-j))*(u[j+4*(r+1)-4]);
			 
			 
		 }
		 b=s[a];
		 for(int j=0; j<4; j++) {
			 v[-1-j+4*(r+1)]=b%2;
			 b=(b-(b%2))/2;
		 }
	 } for(int j=0; j<16; j++) {
		 w[j]=v[p[j+1]-1];
		 w1[j]=v[p[j+1]-1];
		 
	 } 
	 
	 
	 
//	 for(int ar=0; ar<16; ar++) {
//		 System.out.print(u[ar]+",");
//	 } System.out.println();
//	 for(int ar=0; ar<16; ar++) {
//		 System.out.print(v[ar]+",");
//	 }System.out.println();
//	 for(int ar=0; ar<16; ar++) {
//		 System.out.print(w[ar]+",");
//	 }System.out.println();
	 
 }String hurra = ""; for(int i=0; i<16; i++) {
	 hurra+=w[i];
 }
	 return Integer.parseInt(hurra,2);
 }
 
 public static void encrypt3(String k,int[] x) {
	 String[] abc = orgKey(k);
	// System.out.println("\n"+abc[4]);
	 int a = 0;
	 int b = 0;
	 int[] w = new int[16];
	 for(int i=0; i<16;i++)w[i]=x[i];
	 int[] u = new int[16];
	 int[] v = new int[16];
	
	 
	 for(int i=0; i<3; i++) {
		 for(int j=0; j<16; j++) {
			 u[j]=(w[j]+abc[i].charAt(j))%2;
			 
		 }
		 for(int r=0; r<4; r++) {
			 a=0;
		 
		 for(int j=0; j<4; j++) {
			 a = a + (int)(Math.pow(2, 3-j))*(u[j+4*(r+1)-4]);
			 
			 
		 }
		 b=s[a];
		 for(int j=0; j<4; j++) {
			 v[-1-j+4*(r+1)]=b%2;
			 b=(b-(b%2))/2;
		 }
	 } for(int j=0; j<16; j++) {
		 w[j]=v[p[j+1]-1];
		 w1[j]=v[p[j+1]-1];
	 }
		 
	 }
 }
	 
 
 public static void encrypt2(String k) {
		int[] u = new int[16];
		int[] v = new int[16];
	 String[] abc = orgKey(k);
	 int a = 0;
	 int b =0;
	 for (int i=0; i<16; i++) {
		 u[i]=(w1[i]+(int)abc[3].charAt(i))%2;
	 }
	 for(int i=0; i<4; i++) { a=0;	
		 for(int j=0; j<4; j++) {
			 a = a + (int)(Math.pow(2, 3-j))*(u[j+4*(i+1)-4]);
		 }
		 b=s[a];
		 for(int j=0; j<4; j++) {
			 v[-1-j+4*(i+1)]=b%2;
			 b=(b-(b%2))/2;
		 }
	 }
	 for(int arr=0; arr<16; arr++) y[arr]=0;
	 for(int j=0; j<16; j++) {
		 y[j] = (v[j] + (int)abc[4].charAt(j))%2;
	 }
 }
 

	 
 
 public static int decrypt2(String k, int[] n) {
	 String[] abc = orgKey(k);
	 int a = 0;
	 int g = 0;
	 int[] u = new int[16];
	 int[] v = new int[16];
	 int[] w = new int[16];
	 for(int i=0; i<16; i++) {
		 v[i]=(n[i]+abc[4].charAt(i))%2;
	 }
	 for(int i=0; i<4; i++) { a=0;	
	 for(int j=0; j<4; j++) {
		 a = a + (int)(Math.pow(2, 3-j))*(v[j+4*(i+1)-4]);
	 }
	 for(int j=0; j<16; j++) {
		 if(s[j]==a) {
			 g=j;
	 for(int r=0; r<4; r++) {
			 u[-1-r+4*(i+1)]=g%2;
			 g=(g-(g%2))/2;
	 }
		 }
	 }
 
 }
 
 for(int i=0; i<16; i++) {
		 w[i]=(abc[3].charAt(i)+u[i])%2;
	 } 
 for(int i=0; i<16; i++) {
	 v[p[i+1]-1]=w[i];
 }
 for(int i=0; i<4; i++) { a=0;	
 for(int j=0; j<4; j++) {
	 a = a + (int)(Math.pow(2, 3-j))*(v[j+4*(i+1)-4]);
 }
 for(int j=0; j<16; j++) {
	 if(s[j]==a) {
		 g=j;
 for(int r=0; r<4; r++) {
		 u[-1-r+4*(i+1)]=g%2;
		 g=(g-(g%2))/2;
 }
	 }
 }
 

} for(int i=0; i<16; i++) {
	 w[i]=(abc[2].charAt(i)+u[i])%2;
}
String hurra = ""; for(int i=0; i<16; i++) {
	 hurra+=w[i];
}
	 
return Integer.parseInt(hurra,2);

 }
}
 

