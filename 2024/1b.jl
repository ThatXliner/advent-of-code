# using DataStructures
function main()
    # Read all input at once
    input = read(stdin, String)

    # Split input into lines and then split each line into integers
    a = Int[]
    b = Dict()

    for line in split(input, '\n')
        if !isempty(line)
            x, y = parse.(Int, split(line))
            push!(a, x)
            b[y] = get(b,y,0)+1
        end
    end
    output = 0
    for x in a
        output += get(b,x,0) * x
    end
    println(output)
end

main()
