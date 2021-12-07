use crate::AoCDay;
use std::io::{BufRead, BufReader, Read};


pub struct Code;

impl AoCDay for Code {
    fn part1(&self, _input: &mut dyn std::io::Read, _extra_argss: &[String]) -> String {
        let data = BufReader::new(_input)
            .lines()
            .map(|x| x.unwrap())
            .collect::<Vec<String>>();

        let mut x = 0;
        let mut y = 0;
        for s in data {
            let items = s.split_whitespace().collect::<Vec<&str>>();
            let direction = items[0];
            let unit = items[1].parse::<u32>().unwrap();

            match direction {
                "forward" =>  x += unit,
                "down" => y += unit,
                "up" => y -= unit,
                _ => {}
            }
        }

        println!("x={},y={}", x, y);
        return (x * y).to_string()
    }

    fn part2(&self, _input: &mut dyn std::io::Read, _extra_args: &[String]) -> String {
        let data = BufReader::new(_input)
            .lines()
            .map(|x| x.unwrap())
            .collect::<Vec<String>>();

        let mut x = 0;
        let mut y = 0;
        let mut aim = 0;

        for s in data {
            let items = s.split_whitespace().collect::<Vec<&str>>();
            let direction = items[0];
            let unit = items[1].parse::<u32>().unwrap();

            match direction {
                "forward" =>  {
                    x += unit;
                    y += aim * unit;
                },
                "down" => aim += unit,
                "up" => aim-= unit,
                _ => {}
            }
        }

        println!("x={},y={}", x, y);
        return (x * y).to_string()
    }
}
