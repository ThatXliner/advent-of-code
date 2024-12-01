function main()
    # Read all input at once
    input = read(stdin, String)

    # Split input into lines and then split each line into integers
    a = Int[]
    b = Int[]

    for line in split(input, '\n')
        if !isempty(line)
            x, y = parse.(Int, split(line))
            push!(a, x)
            push!(b, y)
        end
    end
    sort!(a)
    sort!(b)
    output = 0
    for i = 1:length(a)
        output += abs(a[i] - b[i])
    end
    println(output)
end

main()
