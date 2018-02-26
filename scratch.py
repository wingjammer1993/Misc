# string alignment implementation

# computes a matrix with optimal alignment costs
def alignStrings(x, y):
    lx = len(x)
    ly = len(y)
    S = [[0 for i in range(ly + 1)] for j in
         range(lx + 1)]  # make a matrix the lengths of the strings + 1, and initialize to 0

    # fill in cost matrix
    for i in range(lx + 1):
        for j in range(ly + 1):
            S[i][j] = cost(S, x, y, i, j)
    # check the matrix values. This prints the columns as rows
    return S


# compute min cost at any given position
def cost(S, x, y, i, j):
    # if we're in initial row or column
    if (i == 0 and j == 0):
        return 0
    elif (i == 0):
        return S[i][j - 1] + 1
    elif (j == 0):
        return S[i - 1][j] + 1

    # initialize return variable and temporary check variable
    mincost = 100
    tmpcost = mincost
    # if chars are the same
    if (x[i - 1] == y[j - 1]):
        mincost = S[i - 1][j - 1]
    # find cost of insert
    tmpcost = S[i - 1][j] + 1
    if (tmpcost < mincost):
        mincost = tmpcost
    # find cost of delete
    tmpcost = S[i][j - 1] + 1
    if (tmpcost < mincost):
        mincost = tmpcost
    # find cost of sub
    tmpcost = S[i - 1][j - 1] + 10
    if (tmpcost < mincost):
        mincost = tmpcost
    # find cost of swap
    tmpcost = S[i - 2][j - 2] + 10
    if (tmpcost < mincost):
        mincost = tmpcost
    return mincost


def extractAlignment(S, x, y):
    # initialize starting indices and vector
    i = len(x)
    j = len(y)
    a = []
    # run through matrix to find optimal vector
    while i > 0 or j > 0:
        a.insert(0, determineOp(S, x, y, i, j))
        [i, j] = updateIJ(a, i, j)
    # return vector with commands
    return a


# function to find optimal operation
def determineOp(S, x, y, i, j):
    # check if swap or sub
    if (i > 0 and j > 0):
        if (S[i - 1][j - 1] < S[i][j - 1] and S[i - 1][j - 1] < S[i - 1][j]):
            if (S[i - 2][j - 2] == S[i][j] - 10):
                return "swap"
            elif (S[i - 1][j - 1] == S[i][j] or S[i - 1][j - 1] == S[i][j] - 10):
                return "sub"
    # check if insert or delete
    if (S[i - 1][j] < S[i][j - 1] or i == 0):
        return "delete"
    else:
        return "insert"


# update indices
def updateIJ(a, i, j):
    # store the command we are using to update
    command = a[0]
    # change indices based on command and return
    if (command == "insert"):
        return [i - 1, j]
    elif (command == "delete"):
        return [i, j - 1]
    elif (command == "swap"):
        return [i - 2, j - 2]
    else:
        return [i - 1, j - 1]


# function to find all common substrings of length L
def commonSub(x, L, a):
    # list of substrings
    substr = []
    # counts consecutive matches (m) and index in string x (x)
    countm = 0
    countx = 0
    # loop thorugh vector to discover substrings
    for i in range(len(a)):
        if (a[i] == "sub" and countm == L - 1):
            substr.append(x[countx - L:countx])
            countx += 1
        elif (a[i] == "sub"):
            countm += 1
            countx += 1
        elif (a[i] == "delete"):
            countm = 0
            countx += 1
        elif (a[i] == "swap"):
            countm = 0
            countx += 1
        else:
            countm = 0
    # return list of substrings
    return substr


if __name__ == "__main__":
    # initialize strings to work with
    str2 = 'the white house office of the press secretary for immediate release march 06, 2017 president trump congratulates exxon mobil for job-creating investment program  washington, d.c. -- president donald j. trump today congratulated exxon mobil corporation on its ambitious $20 billion investment program that is creating more than 45,000 construction and manufacturing jobs in the united states gulf coast region.  president trump made a promise to bring back jobs to america. the spirit of optimism sweeping the country is already boosting job growth, and it is only the beginning.  “this is exactly the kind of investment, economic development and job creation that will help put americans back to work,” the president said. “many of the products that will be manufactured here in the united states by american workers will be exported to other countries, improving our balance of trade. this is a true american success story. in addition, the jobs created are paying on average $100,000 per year.”  darren w. woods, chairman and chief executive officer of exxon mobil announced the company’s investment program during a keynote speech today to an oil and gas industry conference in houston, texas.  “investments of this scale require a pro-growth approach and a stable regulatory environment and we appreciate the president’s commitment to both,” said woods. “the energy industry has proven it can operate safely and responsibly. private sector investment is enhanced by this administration’s support for smart regulations that support growth while protecting the environment.”  exxon mobil is strategically investing in new refining and chemical-manufacturing projects in the united states gulf coast region to expand its manufacturing and export capacity. the company’s growing the gulf program consists of 11 major chemical, refining, lubricant and liquefied natural gas projects at proposed new and existing facilities along the texas and louisiana coasts. investments began in 2013 and are expected to continue through at least 2022.  exxon mobil’s projects, once completed and operating at mature levels, are expected to have far-reaching and long-lasting benefits. projects planned or under way are expected to create more than 35,000 construction jobs and more than 12,000 full-time jobs. these are full-time manufacturing jobs that are mostly high-skilled and high-paying, and have annual salaries ranging from $75,000 to $125,000. these jobs will have a multiplier effect, creating many more jobs in the community that service these new investments.'

    str1 = 'exxonmobil plans investments of $20 billion to expand manufacturing in u.s. gulf region new projects expected to create more than 45,000 high-paying jobs across the region and thousands more through multiplier effect dateline: houston  public company information: nyse:xom  houston--(business wire)--exxon mobil corporation (nyse:xom) is expanding its manufacturing capacity along the u.s. gulf coast through planned investments of $20 billion over a 10-year period to take advantage of the american energy revolution, darren woods, chairman and chief executive officer, said monday.  the projects, at 11 proposed and existing sites, are expected to generate thousands of new high-paying jobs and $20 billion in increased economic activity in texas and louisiana, woods said, highlighting the company’s growing the gulf initiative in a keynote speech today at the ceraweek 2017 conference.  “the united states is a leading producer of oil and natural gas, which is incentivizing u.s. manufacturing to invest and grow,” said woods. “we are using new, abundant domestic energy supplies to provide products to the world at a competitive advantage resulting from lower costs and abundant raw materials. in this way, an upstream technology breakthrough has led to a downstream manufacturing renaissance.”  exxonmobil is strategically investing in new refining and chemical-manufacturing projects in the u.s. gulf coast region to expand its manufacturing and export capacity. the company’s growing the gulf expansion program, consists of 11 major chemical, refining, lubricant and liquefied natural gas projects at proposed new and existing facilities along the texas and louisiana coasts. investments began in 2013 and are expected to continue through at least 2022.  woods said that exxonmobil’s gulf expansion projects are expected to provide long-term economic benefits to the region, noting the creation of direct employment opportunities and the multiplier effects of the company’s investments.  “importantly, growing the gulf also creates jobs and lasting economic benefits for the communities where they’re located,” woods said. “all told, we expect these 11 projects to create over 45,000 jobs. many of these are high-skilled, high-paying jobs averaging about $100,000 a year. and these jobs will have a multiplier effect, creating many more jobs in the communities that service these new investments.”  according to the american chemistry council, chemical manufacturing is one of america’s top exporting industries, accounting for 14 percent of overall u.s. exports in 2015, and exports of specific chemicals linked to shale gas are projected to reach $123 billion by 2030. most of exxonmobil’s planned new chemical capacity investment in the gulf region is targeted toward export markets in asia and elsewhere.  “these projects are export machines, generating products that high-growth nations need to support larger populations with higher standards of living,” woods said. “those overseas markets are the motivation behind our investments. the supply is here; the demand is there. we want to keep connecting those dots.”  about exxonmobil  exxonmobil, the largest publicly traded international oil and gas company, uses technology and innovation to help meet the world’s growing energy needs. exxonmobil holds an industry-leading inventory of resources, is one of the largest refiners and marketers of petroleum products and its chemical company is one of the largest in the world. for more information, visit www.exxonmobil.com or follow us on twitter www.twitter.com/exxonmobil.'

    # choose length of substring to look for
    L = 10
    # get cost matrix, find steps, and print common substrings
    cmat = alignStrings(str1, str2)
    cmdvector = extractAlignment(cmat, str1, str2)
    print(commonSub(str1, L, cmdvector))
