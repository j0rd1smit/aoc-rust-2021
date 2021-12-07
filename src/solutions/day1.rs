use std::io::{BufRead, BufReader, Read};
use crate::AoCDay;

pub struct Code;

impl AoCDay for Code {
    fn part1(&self, _input: &mut dyn std::io::Read, _extra_argss: &[String]) -> String {
        // let mut count = 0;
        // let mut prev = None;
        //
        // let lines = BufReader::new(_input).lines();
        // for line in lines {
        //     let v = line.unwrap().parse::<i32>().unwrap();
        //     if let Some(v_prev) = prev {
        //         if v > v_prev {
        //             count = count + 1;
        //         }
        //     }
        //
        //     prev = Some(v);
        // }
        let data = BufReader::new(_input)
            .lines()
            .map(|x| x.unwrap().parse::<u32>().unwrap())
            .collect::<Vec<u32>>();

        let mut count = 0;
        for i in 1..data.len() {
            if data[i - 1] < data[i] {
                count += 1;
            }
        }

        return count.to_string()
    }



    fn part2(&self, _input: &mut dyn std::io::Read, _extra_args: &[String]) -> String {
        let data = BufReader::new(_input)
            .lines()
            .map(|x| x.unwrap().parse::<u32>().unwrap())
            .collect::<Vec<u32>>();

        let mut count = 0;
        let n = data.len() - 2usize;
        for i in 1..n {
            if data[i - 1] + data[i] + data[i + 1] < data[i] + data[i + 1] + data[i + 2] {
                count += 1;
            }
        }

        return count.to_string()
    }
}

