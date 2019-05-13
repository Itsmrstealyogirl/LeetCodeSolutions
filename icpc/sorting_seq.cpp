#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int n,m,top,map[27][27],indegree[27],outdegree[27],mem[27],s[27];
char str[27],buf[10];
int floyd(){
    int i,j,k;
    for(k=0;k<n;k++)
        for(i=0;i<n;i++)
            for(j=0;j<n;j++){
                if(map[i][k]&&map[k][j]) map[i][j]=1;
            }

    for(i=0;i<n;i++)
        if(map[i][i]) return 0;
    return 1;
}
int calc(){
    int i,j;
    memset(indegree,0,sizeof(indegree));
    memset(outdegree,0,sizeof(outdegree));
    for(i=0;i<n;i++)
        for(j=0;j<n;j++){
            if(map[i][j]) {indegree[j]++;outdegree[i]++;}
        }
    
    for(i=0;i<n;i++) 
        if(indegree[i]+outdegree[i]!=n-1) return 0;
    return 1;
}
void toplogical_sort(){
    int i,j=0;
    top=0;
    for(i=0;i<n&&top<=1;i++) if(!indegree[i]) mem[++top]=i;

    memset(s,0,sizeof(s));

    while(top){
        int cnt=mem[top--];
        s[cnt]=1;
        str[j++]=cnt+'A';
        for(i=0;i<n;i++){
            if(!s[i] && map[cnt][i]) indegree[i]--;
            if(i!=cnt && !s[i] && indegree[i]==0) mem[++top]=i;
        }
    }
    str[j]='\0';
}
int main(){
    while(scanf("%d%d",&n,&m),n&&m){
        memset(map,0,sizeof(map));
        int i,flag1=0,flag2=0;
        for(i=1;i<=m;i++){
            scanf("%s",buf);
            map[buf[0]-'A'][buf[2]-'A']=1;
            if(flag1 || flag2) continue;
            else if(!floyd()) {flag1=i;continue;}
            else if(calc()) {toplogical_sort();flag2=i;}
        }
        if(flag1) printf("Inconsistency found after %d relations.\n",flag1);
        else if(flag2) printf("Sorted sequence determined after %d relations: %s.\n",flag2,str);
        else printf("Sorted sequence cannot be determined.\n");
    }
    return 0;
}