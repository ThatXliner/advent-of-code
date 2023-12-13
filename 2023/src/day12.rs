use std::io::{self, BufRead};

pub fn part1() {
    let stdin = io::stdin();
    let mut total = 0;

    for (l_count, line) in stdin.lock().lines().enumerate() {
        if let Ok(line) = line {
            let mut parts = line.split(" ");
            if let (Some(things), Some(amounts_raw)) = (parts.next(), parts.next()) {
                let amounts: Vec<u32> = amounts_raw
                    .split(",")
                    .filter_map(|x| x.parse().ok())
                    .collect();

                for i in 0..(1 << things.matches('?').count()) {
                    let mut test = things.to_string();

                    for (j, x) in things.chars().enumerate() {
                        if x == '?' {
                            if i & (1 << things[0..j].matches('?').count()) != 0 {
                                test = test.chars().enumerate().map(|(idx, c)| {
                                    if idx == j {
                                        '#'
                                    } else {
                                        c
                                    }
                                }).collect();
                            } else {
                                test = test.chars().enumerate().map(|(idx, c)| {
                                    if idx == j {
                                        '.'
                                    } else {
                                        c
                                    }
                                }).collect();
                            }
                        }
                    }

                    let mut lengths = Vec::new();
                    let re = regex::Regex::new(r"#+").unwrap();
                    for caps in re.captures_iter(&test) {
                        if let Some(mat) = caps.get(0) {
                            lengths.push(mat.as_str().len() as u32);
                        }
                    }

                    println!(
                        "{} {} {} {:?} {:?}",
                        things, i, test, lengths, amounts
                    );

                    if lengths == amounts {
                        total += 1;
                    }
                }
            }
            println!("{} {}", l_count, total);
        }
    }

    println!("{}", total);
}
