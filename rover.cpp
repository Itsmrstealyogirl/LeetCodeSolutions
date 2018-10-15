/*
 * Complete the 'roverMove' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER matrixSize
 *  2. STRING_ARRAY cmds
 */


void moveRover(int &pos, string cmd, int len) {
    if (cmd=="RIGHT" && (pos+1)%len != 0)
        pos++;

    else if (cmd=="LEFT" && (pos%len != 0))
        pos--;

    else if (cmd=="UP" && (pos >= len)) 
        pos -= len;
    else if (cmd=="DOWN" && (pos < (n*(n-1))))
        pos += len;
}


int roverMove(int matrixSize, vector<string> cmds) {
    int pos = 0;
    for (auto cmd : cmds) {
        moveRover(pos,cmd,matrixSize);
    }
    return pos;
}

