bool canAttendMeetings(Interval intervals[], int n) {
    int starts[n];
    int ends[n];
    std::sort(starts);
    std::sort(ends);
    for (int i = 0; i < n-1; i++) {
        if (starts[i+1] < ends[i])
            return false;
    }
    return true;
}
