module Lib
    ( someFunc,
    problem1,
    problem2,
    problem3,
    problem4,
    problem5,
    problem6,
    problem7,
    problem8,
    problem9,
    problem10
    ) where


someFunc :: IO ()
someFunc = putStrLn "enter problemX to run a specific problem"

problem1 :: IO ()
problem1 = putStrLn $ show (prob1 3 5 1 1000)

prob1 div1 div2 start end = helper 0 start where
    helper acc curr | curr == end          = acc
    helper acc curr | curr `mod` div1 == 0 = helper (acc + curr) (curr + 1)
    helper acc curr | curr `mod` div2 == 0 = helper (acc + curr) (curr + 1)
    helper acc curr                        = helper (acc) (curr + 1)




problem2 :: IO ()
problem2 = putStrLn $ show (prob2 2 4000000)


fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

prob2 divisor bound = sum [x | x <- takeWhile (<= bound) fibs, (x `mod` divisor) == 0]



problem3 :: IO ()
problem3 = putStrLn "unimplemented"





problem4 :: IO ()
problem4 = putStrLn "unimplemented"





problem5 :: IO ()
problem5 = putStrLn "unimplemented"





problem6 :: IO ()
problem6 = putStrLn "unimplemented"





problem7 :: IO ()
problem7 = putStrLn "unimplemented"





problem8 :: IO ()
problem8 = putStrLn "unimplemented"





problem9 :: IO ()
problem9 = putStrLn "unimplemented"





problem10 :: IO ()
problem10 = putStrLn "unimplemented"
