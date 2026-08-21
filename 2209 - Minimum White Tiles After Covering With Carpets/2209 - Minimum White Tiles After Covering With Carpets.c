int carlen,flen,nCar;

int minW(int ind,int nc,int memo[flen+1][nCar+1],char* floor,int* white)
{
    if(ind>=flen)
        return 0;
    if(nc==0)
        return white[ind];
    if(memo[ind][nc]!=-1)
    return memo[ind][nc];
    if(floor[ind]=='0')
    memo[ind][nc]= minW(ind+1,nc,memo,floor,white);
    else
    {
    int usingCarpet=minW(ind+carlen,nc-1,memo,floor,white);
    int notusingCarpet=1+minW(ind+1,nc,memo,floor,white);
    memo[ind][nc]= usingCarpet<notusingCarpet?usingCarpet:notusingCarpet;
    }
    return memo[ind][nc];
}


int minimumWhiteTiles(char* floor, int numCarpets, int carpetLen) {
    carlen=carpetLen;
    nCar=numCarpets;
    flen=strlen(floor);
    int white[flen];int w=0;
    for(int i=flen-1;i>=0;i--)
        if(floor[i]=='0')
            white[i]=w;
        else
            white[i]=++w;
    int memo[flen+1][nCar+1];
    for(int i=0;i<=flen;i++)
    for(int j=0;j<=nCar;j++)
    memo[i][j]=-1;
    return minW(0,numCarpets,memo,floor,white);
}