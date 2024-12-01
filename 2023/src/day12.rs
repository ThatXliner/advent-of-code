// Written entirely by ChatGPT, with minor modifications by me
// (the logic is mine but I got ChatGPT to re-write it in Rust)
use lazy_static::lazy_static;
use rayon::prelude::*;
use regex::Regex;
use std::io::{self, BufRead};
lazy_static! {
    static ref RE: Regex = Regex::new(r"#+").unwrap();
}
pub fn part1() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().map(|l| l.unwrap()).collect();
    let total = lines
        .par_iter()
        .fold(
            || 0,
            |acc, line| {
                let mut total_count = acc;
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
                                    test = test
                                        .chars()
                                        .enumerate()
                                        .map(|(idx, c)| if idx == j { '#' } else { c })
                                        .collect();
                                } else {
                                    test = test
                                        .chars()
                                        .enumerate()
                                        .map(|(idx, c)| if idx == j { '.' } else { c })
                                        .collect();
                                }
                            }
                        }

                        let mut lengths = Vec::new();
                        for caps in RE.captures_iter(&test) {
                            if let Some(mat) = caps.get(0) {
                                lengths.push(mat.as_str().len() as u32);
                            }
                        }
                        if lengths == amounts {
                            total_count += 1;
                        }
                    }
                }
                total_count
            },
        )
        .sum::<usize>();

    println!("{}", total);
}
