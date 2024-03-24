# Mark all edges as X
# For all remaining .s do pairwise search and look for pipes
# If that pipe leads to X or out of loop, mark that pair as X and do bfs and mark every adjacent to X
# Add them in visited so that when it comes out of queue again, you have marked it as visited so it won't be part of BFS again